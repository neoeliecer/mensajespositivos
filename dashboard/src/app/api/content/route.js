import { NextResponse } from 'next/server';
import fs from 'fs';
import path from 'path';

const PARENT_DIR = path.resolve(process.cwd(), '../');

export async function GET(request) {
  try {
    const { searchParams } = new URL(request.url);
    const series = searchParams.get('series')?.toLowerCase() || '';
    const chapter = searchParams.get('chapter') || '';
    
    if (!chapter) {
      return NextResponse.json({ error: 'Chapter is required' }, { status: 400 });
    }
    
    // Normalization mappings for series names to match files
    // CSV has "Hágase la Luz" or "luz", "confiar", "respira", "manos", "Recupera tu mente", etc.
    let cleanSeries = series.trim();
    if (cleanSeries.includes('luz') || cleanSeries.includes('hágase') || cleanSeries.includes('hagase')) {
      cleanSeries = 'luz';
    } else if (cleanSeries.includes('confiar')) {
      cleanSeries = 'confiar';
    } else if (cleanSeries.includes('respira')) {
      cleanSeries = 'respira';
    } else if (cleanSeries.includes('manos')) {
      cleanSeries = 'manos';
    } else if (cleanSeries.includes('placebo')) {
      cleanSeries = 'placebo';
    } else if (cleanSeries.includes('musica') || cleanSeries.includes('música')) {
      cleanSeries = 'musica';
    } else if (cleanSeries.includes('recupera') || cleanSeries.includes('mente')) {
      cleanSeries = 'recupera';
    }
    
    const results = {
      script: '',
      post: '',
      resumen: '',
      titles: '',
      coverExists: false,
      coverPath: ''
    };
    
    // File search helper
    const tryReadFile = (fileNames) => {
      for (const name of fileNames) {
        const filePath = path.join(PARENT_DIR, name);
        if (fs.existsSync(filePath)) {
          return fs.readFileSync(filePath, 'utf-8');
        }
      }
      return '';
    };
    
    // Define search patterns depending on the series
    if (cleanSeries === 'luz') {
      results.script = tryReadFile([
        `guion_luz_cap${chapter}_extendido.md`,
        `guion_luz_cap${chapter}.md`,
        `guion_luz_capitulo_${chapter}.md`
      ]);
      results.post = tryReadFile([
        `post_facebook_luz_cap${chapter}.md`,
        `post_facebook_luz_capitulo_${chapter}.md`
      ]);
      results.resumen = tryReadFile([
        `resumen_luz_cap${chapter}.md`
      ]);
      results.titles = tryReadFile([
        `titulos_luz_cap${chapter}.md`,
        `titulos_luz_capitulo_${chapter}.md`
      ]);
    } else if (cleanSeries === 'manos') {
      results.script = tryReadFile([
        `guion_manos_cap${chapter}_extendido.md`,
        `guion_manos_cap${chapter}.md`
      ]);
      results.post = tryReadFile([
        `post_facebook_manos_cap${chapter}.md`
      ]);
      results.resumen = tryReadFile([
        `resumen_manos_cap${chapter}.md`
      ]);
      results.titles = tryReadFile([
        `titulos_manos_cap${chapter}.md`
      ]);
    } else if (cleanSeries === 'respira') {
      results.script = tryReadFile([
        `guion_respira_cap${chapter}_extendido.md`,
        `guion_respira_cap${chapter}.md`
      ]);
      results.post = tryReadFile([
        `post_facebook_respira_cap${chapter}.md`
      ]);
      results.resumen = tryReadFile([
        `resumen_respira_cap${chapter}.md`
      ]);
      results.titles = tryReadFile([
        `titulos_respira_cap${chapter}.md`,
        `titulos_respira_anexo.md`
      ]);
    } else if (cleanSeries === 'confiar') {
      results.script = tryReadFile([
        `guion_confiar_cap${chapter}_extendido.md`,
        `guion_confiar_cap${chapter}.md`
      ]);
      results.post = tryReadFile([
        `post_facebook_confiar_cap${chapter}.md`
      ]);
      results.resumen = tryReadFile([
        `resumen_confiar_cap${chapter}.md`
      ]);
      results.titles = tryReadFile([
        `titulos_confiar_cap${chapter}.md`
      ]);
    } else if (cleanSeries === 'placebo') {
      results.script = tryReadFile([
        `guion_placebo_capitulo_${chapter}.md`,
        `guion_placebo_cap${chapter}.md`
      ]);
      results.post = tryReadFile([
        `post_facebook_placebo_capitulo_${chapter}.md`
      ]);
    } else if (cleanSeries === 'musica') {
      results.script = tryReadFile([
        `guion_musica_capitulo_${chapter}.md`
      ]);
      results.post = tryReadFile([
        `post_facebook_musica_capitulo_${chapter}.md`
      ]);
    } else {
      // Default / Recupera tu mente patterns
      results.script = tryReadFile([
        `guion_capitulo_${chapter}.md`,
        `guion_luz_cap${chapter}.md`,
        `guion_${cleanSeries}_cap${chapter}.md`
      ]);
      results.post = tryReadFile([
        `post_facebook_capitulo_${chapter}.md`,
        `post_facebook_luz_cap${chapter}.md`,
        `post_facebook_${cleanSeries}_cap${chapter}.md`
      ]);
      results.titles = tryReadFile([
        `titulos_capitulo_${chapter}.md`,
        `titulos_luz_cap${chapter}.md`
      ]);
    }
    
    // Check if cover image exists
    const coverPatterns = [
      `portada_capitulo_${chapter}.png`,
      `portada_capitulo_${chapter}_creative.png`,
      `portada_luz_cap${chapter}.png`,
      `portada_manos_cap${chapter}.png`,
      `portada_${cleanSeries}_cap${chapter}.png`,
      `portada_musica_capitulo_${chapter}.png`,
      `portada_placebo_capitulo_${chapter}_con_titulo.png`
    ];
    
    for (const pattern of coverPatterns) {
      const coverPath = path.join(PARENT_DIR, pattern);
      if (fs.existsSync(coverPath)) {
        results.coverExists = true;
        results.coverPath = pattern; // Relative path from root
        break;
      }
    }
    
    return NextResponse.json(results);
  } catch (err) {
    return NextResponse.json({ error: err.message }, { status: 500 });
  }
}
