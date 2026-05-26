
import os
import csv
import time
import sys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import pyperclip

# Configuration
CSV_FILE = r'c:\Users\neo\Documents\agente\mensajes positivos\content_calendar.csv'
USER_DATA_DIR = r'c:\Users\neo\AppData\Local\Google\Chrome\User Data' # Update if using a different profile
PROFILE_DIRECTORY = "Default" 

def update_csv_status(chapter_num, new_status):
    """Updates the status in the CSV file safely."""
    rows = []
    with open(CSV_FILE, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        for row in reader:
            if row['Chapter'] == str(chapter_num):
                row['Status'] = new_status
            rows.append(row)

    with open(CSV_FILE, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    print(f"Updated Chapter {chapter_num} status to '{new_status}'")

def setup_driver():
    """Sets up the Chrome driver with user profile."""
    options = Options()
    # options.add_argument(f"user-data-dir={USER_DATA_DIR}")
    # options.add_argument(f"profile-directory={PROFILE_DIRECTORY}")
    options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")
    
    # Using webdriver_manager to handle driver installation
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    return driver

def post_to_facebook(driver, video_path, caption):
    """Navigates to Facebook and uploads the video."""
    try:
        driver.get("https://www.facebook.com/")
        time.sleep(5)

        # Check for login (simple check)
        if "login" in driver.current_url:
            print("Please log in manually in the browser window within 60 seconds...")
            WebDriverWait(driver, 60).until(lambda d: "facebook.com/" in d.current_url and "login" not in d.current_url)
            print("Login detected!")

        # Go to creator studio or specific post page - for personal profiles, main feed is easiest for now
        # Ideally, we should use Business Suite for pages, but let's start simple with personal/page feed
        
        # Click on "Photo/video" input
        print("Looking for post input...")
        
        # Different selectors might work depending on Facebook's A/B testing
        # 1. Try finding the input of type file directly if possible (hidden)
        # file_input = driver.find_element(By.XPATH, "//input[@type='file']")
        # file_input.send_keys(video_path)
        
        # 2. Clicking the "What's on your mind?" area first
        try:
             # This is tricky as classes change. Searching by text or aria-label is safer.
             create_post_area = WebDriverWait(driver, 10).until(
                 EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), \"What's on your mind\")] | //span[contains(text(), \"¿Qué estás pensando\")]"))
             )
             create_post_area.click()
             time.sleep(2)
        except Exception as e:
            print(f"Could not click 'What's on your mind': {e}")
            # Try alternative: "Photo/Video" button directly
            pass

        # Find the photo/video button/icon
        print("Selecting photo/video...")
        try:
            photo_video_button = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//div[@aria-label='Photo/video' or @aria-label='Foto/video']"))
            )
            photo_video_button.click()
            time.sleep(2)
            
            # Now we need to send the file path to the hidden input
            # Usually creates a file input after clicking
            file_inputs = driver.find_elements(By.XPATH, "//input[@type='file']")
            if file_inputs:
                file_inputs[-1].send_keys(video_path)
                print(f"Uploading video: {video_path}")
            else:
                 print("Could not find file input element.")
                 return False

        except Exception as e:
             print(f"Error selecting photo/video: {e}")
             return False
        
        # Wait for video to be "ready" or at least for the caption box to appear
        time.sleep(5)
        
        # Enter Caption
        print("Entering caption...")
        try:
            # Clipboard method is often more reliable for emojis and complex text than send_keys
            pyperclip.copy(caption)
            
            active_element = driver.switch_to.active_element
            active_element.send_keys(Keys.CONTROL, 'v') # Paste
            print("Caption pasted.")
        except Exception as e:
            print(f"Error entering caption: {e}")
            # heavy fallback: find the input box
            pass

        # Click Post
        print("Clicking Post button...")
        try:
            post_button = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, "//div[@aria-label='Post' or @aria-label='Publicar']"))
            )
            # Check if enabled
            if post_button.get_attribute("aria-disabled") == "true":
                print("Post button disabled (maybe video uploading?). Waiting...")
                time.sleep(10)
            
            post_button.click()
            print("Post button clicked!")
            
            # Wait for upload to catch up (important for videos)
            print("Waiting for upload to finish (this keeps the browser open)...")
            # We can monitor for a specific "Posting..." notification or just wait a safe amount
            time.sleep(30) 
            
            return True

        except Exception as e:
            print(f"Error publishing: {e}")
            return False

    except Exception as e:
        print(f"An error occurred: {e}")
        return False

def main():
    rows_to_process = []
    with open(CSV_FILE, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['Status'] == 'Ready for Video' and row['Video_Path']:
                 rows_to_process.append(row)
    
    if not rows_to_process:
        print("No rows found with status 'Ready for Video' and a valid Video_Path.")
        return

    print(f"Found {len(rows_to_process)} posts to process.")
    
    driver = setup_driver()
    
    try:
        for row in rows_to_process:
            print(f"Processing Chapter {row['Chapter']}...")
            if post_to_facebook(driver, row['Video_Path'], row['Facebook_Post_Text']):
                update_csv_status(row['Chapter'], "Published")
                print("Successfully processed!")
                # Wait a bit between posts
                time.sleep(10)
            else:
                print("Failed to process.")
                
    finally:
        print("Closing driver in 10 seconds...")
        time.sleep(10)
        driver.quit()

if __name__ == "__main__":
    from selenium.webdriver.common.keys import Keys # local import
    main()
