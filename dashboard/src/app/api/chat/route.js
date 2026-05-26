import { NextResponse } from 'next/server';
import { GoogleGenAI } from '@google/generative-ai';
import fs from 'fs';
import path from 'path';

const AGENT_PROFILE_PATH = path.resolve(process.cwd(), '../agent_profile.md');
const ENV_PATH = path.resolve(process.cwd(), '.env.local');

// Helper to get Gemini API key
function getApiKey() {
  // 1. Try env variable
  if (process.env.GEMINI_API_KEY) {
    return process.env.GEMINI_API_KEY;
  }
  
  // 2. Try .env.local file in dashboard directory
  if (fs.existsSync(ENV_PATH)) {
    const envContent = fs.readFileSync(ENV_PATH, 'utf-8');
    const match = envContent.match(/GEMINI_API_KEY\s*=\s*(.*)/);
    if (match && match[1]) {
      return match[1].trim();
    }
  }
  
  return null;
}

export async function POST(request) {
  try {
    const { messages } = await request.json();
    
    if (!messages || !Array.isArray(messages)) {
      return NextResponse.json({ error: 'Messages are required' }, { status: 400 });
    }
    
    const apiKey = getApiKey();
    if (!apiKey || apiKey === 'YOUR_GEMINI_API_KEY_HERE') {
      return NextResponse.json({ 
        error: 'API_KEY_MISSING',
        message: 'No se encontró la clave de API de Gemini. Por favor, crea un archivo `.env.local` en la carpeta `dashboard` con la línea `GEMINI_API_KEY=tu_clave_api`' 
      }, { status: 400 });
    }
    
    // Load System prompt / Agent instructions
    let systemInstruction = 'Eres un experto editor de crecimiento personal y guionista de YouTube/Redes Sociales.';
    if (fs.existsSync(AGENT_PROFILE_PATH)) {
      try {
        const agentProfile = fs.readFileSync(AGENT_PROFILE_PATH, 'utf-8');
        systemInstruction = `Instrucciones del Perfil del Agente:\n\n${agentProfile}\n\nActúa estrictamente bajo este perfil en todas tus respuestas. Usa español en un tono emotivo, inspirador y cercano.`;
      } catch (err) {
        console.error('Error loading agent profile', err);
      }
    }
    
    // Initialize Google Gen AI
    const ai = new GoogleGenAI({ apiKey });
    
    // Format messages for the Gemini SDK
    // The official Gemini SDK expects: { role: 'user' | 'model', parts: [{ text: '...' }] }
    const geminiHistory = messages.map(msg => ({
      role: msg.role === 'assistant' ? 'model' : 'user',
      parts: [{ text: msg.content }]
    }));
    
    // The last message is the current prompt, and the previous ones form the history
    const currentPrompt = geminiHistory[geminiHistory.length - 1].parts[0].text;
    const history = geminiHistory.slice(0, -1);
    
    const chat = ai.chats.create({
      model: 'gemini-2.5-flash', // Using latest gemini-2.5-flash
      config: {
        systemInstruction,
        temperature: 0.7,
      },
      history
    });
    
    const result = await chat.sendMessage({ message: currentPrompt });
    const replyText = result.text;
    
    return NextResponse.json({ 
      role: 'assistant', 
      content: replyText 
    });
  } catch (err) {
    return NextResponse.json({ error: err.message }, { status: 500 });
  }
}
