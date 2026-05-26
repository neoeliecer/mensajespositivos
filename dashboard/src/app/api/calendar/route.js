import { NextResponse } from 'next/server';
import fs from 'fs';
import path from 'path';

const CSV_PATH = path.resolve(process.cwd(), '../content_calendar.csv');

// Robust CSV Parser that handles double quotes, escaped quotes, and newlines in values
function parseCSV(text) {
  const result = [];
  let row = [];
  let cell = '';
  let inQuotes = false;
  
  for (let i = 0; i < text.length; i++) {
    const char = text[i];
    const nextChar = text[i + 1];
    
    if (inQuotes) {
      if (char === '"') {
        if (nextChar === '"') {
          cell += '"';
          i++; // Skip next quote
        } else {
          inQuotes = false; // End of quote
        }
      } else {
        cell += char;
      }
    } else {
      if (char === '"') {
        inQuotes = true;
      } else if (char === ',') {
        row.push(cell.trim());
        cell = '';
      } else if (char === '\r') {
        // Skip CR
      } else if (char === '\n') {
        row.push(cell.trim());
        result.push(row);
        row = [];
        cell = '';
      } else {
        cell += char;
      }
    }
  }
  
  if (cell || row.length > 0) {
    row.push(cell.trim());
    result.push(row);
  }
  
  return result;
}

// Convert JSON array back to CSV string
function toCSV(data) {
  return data.map(row => {
    return row.map(cell => {
      let val = cell === undefined || cell === null ? '' : String(cell);
      if (val.includes(',') || val.includes('"') || val.includes('\n') || val.includes('\r')) {
        val = `"${val.replace(/"/g, '""')}"`;
      }
      return val;
    }).join(',');
  }).join('\n');
}

export async function GET() {
  try {
    if (!fs.existsSync(CSV_PATH)) {
      return NextResponse.json({ error: 'Calendar CSV not found' }, { status: 404 });
    }
    
    const content = fs.readFileSync(CSV_PATH, 'utf-8');
    const rows = parseCSV(content);
    
    if (rows.length === 0) {
      return NextResponse.json([]);
    }
    
    const headers = rows[0].map(h => h.trim());
    const data = [];
    
    for (let i = 1; i < rows.length; i++) {
      const row = rows[i];
      // Skip empty rows
      if (row.length === 0 || (row.length === 1 && row[0] === '')) continue;
      
      const item = {};
      headers.forEach((header, index) => {
        item[header || `col_${index}`] = row[index] || '';
      });
      // Add id for easier tracking in UI
      item.id = i;
      data.push(item);
    }
    
    return NextResponse.json({ headers, data });
  } catch (err) {
    return NextResponse.json({ error: err.message }, { status: 500 });
  }
}

export async function POST(request) {
  try {
    const { action, payload } = await request.json();
    
    if (!fs.existsSync(CSV_PATH)) {
      return NextResponse.json({ error: 'Calendar CSV not found' }, { status: 404 });
    }
    
    const content = fs.readFileSync(CSV_PATH, 'utf-8');
    const rows = parseCSV(content);
    const headers = rows[0].map(h => h.trim());
    
    if (action === 'update_row') {
      const { id, updatedData } = payload;
      // id maps to the index in the original rows array (which is 1-indexed)
      if (id && id < rows.length) {
        const row = rows[id];
        headers.forEach((header, index) => {
          if (updatedData[header] !== undefined) {
            row[index] = updatedData[header];
          }
        });
        
        fs.writeFileSync(CSV_PATH, toCSV(rows), 'utf-8');
        return NextResponse.json({ success: true, message: 'Row updated successfully' });
      } else {
        return NextResponse.json({ error: 'Row ID invalid' }, { status: 400 });
      }
    }
    
    if (action === 'add_row') {
      const newRow = headers.map(header => payload[header] || '');
      rows.push(newRow);
      
      fs.writeFileSync(CSV_PATH, toCSV(rows), 'utf-8');
      return NextResponse.json({ success: true, message: 'Row added successfully' });
    }
    
    return NextResponse.json({ error: 'Invalid action' }, { status: 400 });
  } catch (err) {
    return NextResponse.json({ error: err.message }, { status: 500 });
  }
}
