'use client';

import React, { useState, useEffect, useRef } from 'react';
import { 
  LayoutDashboard, 
  Calendar as CalendarIcon, 
  MessageSquare, 
  Sparkles, 
  BookOpen, 
  Clock, 
  Check, 
  Copy, 
  Save, 
  Search, 
  Filter, 
  ChevronRight, 
  Image as ImageIcon, 
  AlertCircle, 
  X, 
  Send,
  Loader2,
  FileText,
  AlertTriangle,
  RotateCcw
} from 'lucide-react';

/* ----------------------------------------------------
   FRONTEND UTILITY: SIMPLE MARKDOWN RENDERER
   ---------------------------------------------------- */
function renderMarkdown(text) {
  if (!text) return <p className="text-gray-400 italic">No hay contenido disponible.</p>;
  
  const lines = text.split('\n');
  return (
    <div className="markdown-body">
      {lines.map((line, idx) => {
        const cleanLine = line.trim();
        
        if (cleanLine.startsWith('# ')) {
          return <h1 key={idx} className="text-2xl font-bold text-white mt-6 mb-3 border-b border-purple-950 pb-2">{cleanLine.slice(2)}</h1>;
        }
        if (cleanLine.startsWith('## ')) {
          return <h2 key={idx} className="text-xl font-semibold text-purple-200 mt-5 mb-2">{cleanLine.slice(3)}</h2>;
        }
        if (cleanLine.startsWith('### ')) {
          return <h3 key={idx} className="text-lg font-semibold text-purple-300 mt-4 mb-2">{cleanLine.slice(4)}</h3>;
        }
        if (cleanLine.startsWith('> ')) {
          return (
            <blockquote key={idx} className="border-l-4 border-purple-500 pl-4 py-3 my-4 italic text-purple-100 bg-purple-950/20 rounded-r-md">
              {cleanLine.slice(2).replace(/\*(.*?)\*/g, '$1')}
            </blockquote>
          );
        }
        if (cleanLine.startsWith('* ') || cleanLine.startsWith('- ')) {
          const listContent = cleanLine.slice(2)
            .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
            .replace(/\*(.*?)\*/g, '<em>$1</em>');
          return <li key={idx} className="ml-6 list-disc text-purple-200/90 my-1.5" dangerouslySetInnerHTML={{ __html: listContent }} />;
        }
        if (cleanLine === '') {
          return <div key={idx} className="h-2" />;
        }
        
        let formatted = line
          .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
          .replace(/\*(.*?)\*/g, '<em>$1</em>')
          .replace(/`([^`]+)`/g, '<code class="bg-purple-950/60 px-1.5 py-0.5 rounded text-purple-300 font-mono text-sm">$1</code>');
          
        return <p key={idx} className="text-purple-200/80 my-2 leading-relaxed" dangerouslySetInnerHTML={{ __html: formatted }} />;
      })}
    </div>
  );
}

export default function Dashboard() {
  // Navigation State
  const [activeTab, setActiveTab] = useState('dashboard'); // 'dashboard' | 'calendar' | 'chat'
  
  // Calendar & Content State
  const [headers, setHeaders] = useState([]);
  const [calendarData, setCalendarData] = useState([]);
  const [loading, setLoading] = useState(true);
  const [searchQuery, setSearchQuery] = useState('');
  const [filterBook, setFilterBook] = useState('All');
  const [filterStatus, setFilterStatus] = useState('All');
  
  // Selection / Editing State
  const [selectedRow, setSelectedRow] = useState(null);
  const [detailContent, setDetailContent] = useState({
    script: '',
    post: '',
    resumen: '',
    coverExists: false,
    coverPath: ''
  });
  const [loadingContent, setLoadingContent] = useState(false);
  const [editFields, setEditFields] = useState({
    Titulo: '',
    Fecha_Publicacion: '',
    Estado: '',
    Texto_Post: ''
  });
  const [savingRow, setSavingRow] = useState(false);
  const [copySuccess, setCopySuccess] = useState(false);
  
  // Chat State
  const [chatMessages, setChatMessages] = useState([
    { role: 'assistant', content: '¡Hola! Soy tu Agente de Contenidos Reflexivos. ¿En qué puedo ayudarte hoy? Podemos crear nuevos guiones, revisar posts de Facebook, calendarizar lanzamientos o conversar sobre las enseñanzas de tus libros favoritos.' }
  ]);
  const [chatInput, setChatInput] = useState('');
  const [chatLoading, setChatLoading] = useState(false);
  const [chatError, setChatError] = useState(null);
  const chatEndRef = useRef(null);

  // Fetch Calendar Data
  const fetchCalendar = async () => {
    try {
      setLoading(true);
      const res = await fetch('/api/calendar');
      const data = await res.json();
      if (data && data.headers) {
        setHeaders(data.headers);
        setCalendarData(data.data);
      }
    } catch (err) {
      console.error('Error fetching calendar', err);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchCalendar();
  }, []);

  // Scroll to bottom of chat
  useEffect(() => {
    chatEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [chatMessages]);

  // Load Scripts and Posts for Selected Row
  const loadRowContent = async (row) => {
    try {
      setLoadingContent(true);
      setSelectedRow(row);
      setEditFields({
        Titulo: row.Titulo || '',
        Fecha_Publicacion: row.Fecha_Publicacion || '',
        Estado: row.Estado || 'Draft',
        Texto_Post: row.Texto_Post || ''
      });
      
      const res = await fetch(`/api/content?series=${encodeURIComponent(row.Libro)}&chapter=${encodeURIComponent(row.Capitulo)}`);
      const data = await res.json();
      setDetailContent(data);
    } catch (err) {
      console.error('Error loading content', err);
    } finally {
      setLoadingContent(false);
    }
  };

  // Save Row Updates
  const handleSaveRow = async () => {
    if (!selectedRow) return;
    try {
      setSavingRow(true);
      const res = await fetch('/api/calendar', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          action: 'update_row',
          payload: {
            id: selectedRow.id,
            updatedData: editFields
          }
        })
      });
      const data = await res.json();
      if (data.success) {
        // Refresh local state
        setCalendarData(prev => prev.map(item => 
          item.id === selectedRow.id ? { ...item, ...editFields } : item
        ));
        
        // Update selected row
        setSelectedRow(prev => ({ ...prev, ...editFields }));
      }
    } catch (err) {
      console.error('Error saving row', err);
    } finally {
      setSavingRow(false);
    }
  };

  // Copy to Clipboard Utility
  const copyToClipboard = (text) => {
    navigator.clipboard.writeText(text);
    setCopySuccess(true);
    setTimeout(() => setCopySuccess(false), 2000);
  };

  // Send Message to Agent Chat
  const handleSendMessage = async (e) => {
    e?.preventDefault();
    if (!chatInput.trim() || chatLoading) return;
    
    const userMsg = { role: 'user', content: chatInput };
    setChatMessages(prev => [...prev, userMsg]);
    setChatInput('');
    setChatLoading(true);
    setChatError(null);
    
    try {
      const res = await fetch('/api/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          messages: [...chatMessages, userMsg]
        })
      });
      
      const data = await res.json();
      
      if (res.status === 400 && data.error === 'API_KEY_MISSING') {
        setChatError(data.message);
        setChatMessages(prev => [...prev, {
          role: 'assistant',
          content: '⚠️ **Error de Configuración:** Por favor, asegúrate de colocar tu clave de API de Gemini en el archivo `.env.local` dentro de la carpeta `dashboard` para habilitar el chat interactivo en vivo.'
        }]);
      } else if (!res.ok) {
        throw new Error(data.error || 'Fallo al comunicarse con Gemini');
      } else {
        setChatMessages(prev => [...prev, { role: 'assistant', content: data.content }]);
      }
    } catch (err) {
      setChatError(err.message);
      setChatMessages(prev => [...prev, {
        role: 'assistant',
        content: `❌ Hubo un error de conexión al procesar tu solicitud: *${err.message}*. Revisa que el servidor local Next.js tenga salida a internet.`
      }]);
    } finally {
      setChatLoading(false);
    }
  };

  // Statistics Computations
  const totalChapters = calendarData.length;
  const publishedCount = calendarData.filter(item => item.Estado?.toLowerCase() === 'publicado').length;
  const pendingCount = calendarData.filter(item => item.Estado?.toLowerCase() === 'pendiente').length;
  const draftCount = calendarData.filter(item => item.Estado?.toLowerCase() === 'draft' || !item.Estado).length;
  const uniqueBooks = Array.from(new Set(calendarData.map(item => item.Libro).filter(Boolean)));

  // Filter and Search Logic
  const filteredData = calendarData.filter(item => {
    const matchesSearch = 
      (item.Titulo || '').toLowerCase().includes(searchQuery.toLowerCase()) ||
      (item.Texto_Post || '').toLowerCase().includes(searchQuery.toLowerCase()) ||
      (item.Libro || '').toLowerCase().includes(searchQuery.toLowerCase());
    
    const matchesBook = filterBook === 'All' || item.Libro === filterBook;
    
    const matchesStatus = filterStatus === 'All' || 
      (filterStatus === 'Draft' && (item.Estado === 'Draft' || !item.Estado)) ||
      item.Estado === filterStatus;
      
    return matchesSearch && matchesBook && matchesStatus;
  });

  return (
    <div className="glass-container">
      {/* ----------------------------------------------------
         SIDEBAR NAVIGATION
         ---------------------------------------------------- */}
      <aside className="sidebar">
        <div className="flex items-center gap-3 mb-8 px-2">
          <div className="bg-purple-600/20 p-2 rounded-xl border border-purple-500/30">
            <Sparkles className="w-6 h-6 text-purple-400" />
          </div>
          <div>
            <h1 className="font-bold text-white text-lg leading-tight">Positivos</h1>
            <span className="text-xs text-purple-400 font-semibold tracking-widest uppercase">Dashboard v1.0</span>
          </div>
        </div>

        <nav className="flex-1 flex flex-col gap-2">
          <button 
            onClick={() => setActiveTab('dashboard')}
            className={`flex items-center gap-3 px-4 py-3 rounded-xl transition-all duration-300 font-medium ${
              activeTab === 'dashboard' 
                ? 'bg-purple-600 text-white shadow-lg shadow-purple-900/30' 
                : 'text-purple-300/70 hover:bg-purple-950/20 hover:text-purple-200'
            }`}
          >
            <LayoutDashboard className="w-5 h-5" />
            <span>Dashboard</span>
          </button>
          
          <button 
            onClick={() => setActiveTab('calendar')}
            className={`flex items-center gap-3 px-4 py-3 rounded-xl transition-all duration-300 font-medium ${
              activeTab === 'calendar' 
                ? 'bg-purple-600 text-white shadow-lg shadow-purple-900/30' 
                : 'text-purple-300/70 hover:bg-purple-950/20 hover:text-purple-200'
            }`}
          >
            <CalendarIcon className="w-5 h-5" />
            <span>Calendario</span>
          </button>
          
          <button 
            onClick={() => setActiveTab('chat')}
            className={`flex items-center gap-3 px-4 py-3 rounded-xl transition-all duration-300 font-medium ${
              activeTab === 'chat' 
                ? 'bg-purple-600 text-white shadow-lg shadow-purple-900/30' 
                : 'text-purple-300/70 hover:bg-purple-950/20 hover:text-purple-200'
            }`}
          >
            <MessageSquare className="w-5 h-5" />
            <span>Chat con Agente</span>
          </button>
        </nav>

        <div className="bg-purple-950/20 border border-purple-900/40 rounded-2xl p-4 mt-auto">
          <h4 className="text-xs font-semibold text-purple-300 mb-1">Servidor Local</h4>
          <div className="flex items-center gap-2 text-xs text-emerald-400">
            <span className="w-2.5 h-2.5 rounded-full bg-emerald-500 animate-pulse"></span>
            <span>En línea - Puerto 3000</span>
          </div>
        </div>
      </aside>

      {/* ----------------------------------------------------
         MAIN PANEL CONTENT
         ---------------------------------------------------- */}
      <main className="main-content">
        
        {/* ------------------ DASHBOARD TAB ------------------ */}
        {activeTab === 'dashboard' && (
          <div className="animate-in fade-in slide-in-from-bottom-4 duration-500">
            <header className="mb-8">
              <h2 className="text-3xl font-extrabold text-white tracking-tight">Tu Creador de Contenidos</h2>
              <p className="text-purple-300/60 mt-1">Resumen del estado de tus libros y publicaciones para redes sociales.</p>
            </header>

            {/* Grid Stats */}
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-8">
              <div className="glass-card p-6 flex items-center justify-between">
                <div>
                  <span className="text-xs font-semibold tracking-wider text-purple-400 uppercase">Capítulos Totales</span>
                  <h3 className="text-3xl font-extrabold text-white mt-1">{totalChapters}</h3>
                </div>
                <div className="bg-purple-500/10 p-3 rounded-xl border border-purple-500/25">
                  <BookOpen className="w-6 h-6 text-purple-400" />
                </div>
              </div>

              <div className="glass-card p-6 flex items-center justify-between">
                <div>
                  <span className="text-xs font-semibold tracking-wider text-purple-400 uppercase">Publicados</span>
                  <h3 className="text-3xl font-extrabold text-emerald-400 mt-1">{publishedCount}</h3>
                </div>
                <div className="bg-emerald-500/10 p-3 rounded-xl border border-emerald-500/25">
                  <Check className="w-6 h-6 text-emerald-400" />
                </div>
              </div>

              <div className="glass-card p-6 flex items-center justify-between">
                <div>
                  <span className="text-xs font-semibold tracking-wider text-purple-400 uppercase">Programados / Pendientes</span>
                  <h3 className="text-3xl font-extrabold text-yellow-400 mt-1">{pendingCount}</h3>
                </div>
                <div className="bg-yellow-500/10 p-3 rounded-xl border border-yellow-500/25">
                  <Clock className="w-6 h-6 text-yellow-400" />
                </div>
              </div>

              <div className="glass-card p-6 flex items-center justify-between">
                <div>
                  <span className="text-xs font-semibold tracking-wider text-purple-400 uppercase">Borradores</span>
                  <h3 className="text-3xl font-extrabold text-purple-300 mt-1">{draftCount}</h3>
                </div>
                <div className="bg-purple-950/30 p-3 rounded-xl border border-purple-900/30">
                  <FileText className="w-6 h-6 text-purple-300" />
                </div>
              </div>
            </div>

            <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
              {/* Active Books list */}
              <div className="glass-card p-6 lg:col-span-2">
                <h3 className="text-xl font-bold text-white mb-4 flex items-center gap-2">
                  <BookOpen className="w-5 h-5 text-purple-400" />
                  <span>Libros Activos en el Sistema</span>
                </h3>
                <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                  {uniqueBooks.map(book => {
                    const bookChapters = calendarData.filter(i => i.Libro === book);
                    const bookPublished = bookChapters.filter(i => i.Estado?.toLowerCase() === 'publicado').length;
                    const pct = bookChapters.length > 0 ? Math.round((bookPublished / bookChapters.length) * 100) : 0;
                    
                    return (
                      <div key={book} className="bg-purple-950/15 border border-purple-900/30 p-4 rounded-xl">
                        <div className="flex justify-between items-start mb-2">
                          <h4 className="font-bold text-purple-200 text-sm truncate max-w-[180px]">{book}</h4>
                          <span className="text-xs font-bold text-purple-400">{pct}% Listo</span>
                        </div>
                        <div className="w-full bg-purple-950/40 h-2 rounded-full overflow-hidden mb-3">
                          <div className="bg-purple-600 h-full rounded-full transition-all duration-500" style={{ width: `${pct}%` }}></div>
                        </div>
                        <div className="flex justify-between text-xs text-purple-300/60">
                          <span>{bookChapters.length} Capítulos</span>
                          <span>{bookPublished} Publicados</span>
                        </div>
                      </div>
                    );
                  })}
                </div>
              </div>

              {/* Automation Control Panel */}
              <div className="glass-card p-6 flex flex-col justify-between">
                <div>
                  <h3 className="text-xl font-bold text-white mb-3 flex items-center gap-2">
                    <Sparkles className="w-5 h-5 text-purple-400" />
                    <span>Automatización</span>
                  </h3>
                  <p className="text-xs text-purple-300/60 leading-relaxed mb-4">
                    Puedes extraer y generar el guion literario de voz en off, el post de Facebook y la sugerencia de portada para el próximo capítulo del libro en curso.
                  </p>
                  
                  <div className="bg-purple-950/30 border border-purple-900/40 rounded-xl p-3 mb-4">
                    <div className="text-xs text-purple-300 font-semibold mb-1">Serie en Curso</div>
                    <div className="text-sm font-bold text-white">Hágase la Luz</div>
                    <div className="text-xs text-purple-400/80 mt-0.5">Último procesado: Capítulo 18</div>
                  </div>
                </div>

                <button 
                  onClick={() => {
                    setActiveTab('chat');
                    setChatInput('Procesa el siguiente capítulo de Hágase la Luz de forma automática.');
                  }}
                  className="btn-primary w-full py-3"
                >
                  <Sparkles className="w-4 h-4" />
                  <span>Procesar Próximo Capítulo</span>
                </button>
              </div>
            </div>
          </div>
        )}

        {/* ------------------ CALENDAR TAB ------------------ */}
        {activeTab === 'calendar' && (
          <div className="animate-in fade-in slide-in-from-bottom-4 duration-500">
            <header className="mb-6">
              <h2 className="text-3xl font-extrabold text-white tracking-tight">Calendario Editorial</h2>
              <p className="text-purple-300/60 mt-1">Modifica las publicaciones del calendario, visualiza los guiones listos y programa fechas.</p>
            </header>

            {/* Filter and Search Bar */}
            <div className="grid grid-cols-1 md:grid-cols-3 lg:grid-cols-4 gap-4 mb-6">
              <div className="relative">
                <Search className="absolute left-3 top-3.5 w-4 h-4 text-purple-400" />
                <input 
                  type="text" 
                  placeholder="Buscar capítulo o contenido..."
                  value={searchQuery}
                  onChange={(e) => setSearchQuery(e.target.value)}
                  className="form-input w-full pl-10"
                />
              </div>

              <div className="flex items-center gap-2">
                <Filter className="w-4 h-4 text-purple-400" />
                <select 
                  value={filterBook} 
                  onChange={(e) => setFilterBook(e.target.value)}
                  className="form-input flex-1"
                >
                  <option value="All">Todos los Libros</option>
                  {uniqueBooks.map(b => <option key={b} value={b}>{b}</option>)}
                </select>
              </div>

              <div className="flex items-center gap-2">
                <Clock className="w-4 h-4 text-purple-400" />
                <select 
                  value={filterStatus} 
                  onChange={(e) => setFilterStatus(e.target.value)}
                  className="form-input flex-1"
                >
                  <option value="All">Todos los Estados</option>
                  <option value="Draft">Draft (Borrador)</option>
                  <option value="pendiente">Pendiente</option>
                  <option value="publicado">Publicado</option>
                </select>
              </div>
              
              <button 
                onClick={() => {
                  setSearchQuery('');
                  setFilterBook('All');
                  setFilterStatus('All');
                }}
                className="btn-secondary py-2 justify-center"
              >
                <RotateCcw className="w-4 h-4" />
                <span>Restablecer</span>
              </button>
            </div>

            <div className="grid grid-cols-1 xl:grid-cols-3 gap-8 items-start">
              {/* Table Wrapper */}
              <div className="glass-card p-4 xl:col-span-2 overflow-x-auto">
                {loading ? (
                  <div className="flex flex-col items-center justify-center py-20 gap-3">
                    <Loader2 className="w-8 h-8 text-purple-500 animate-spin" />
                    <span className="text-purple-300/50">Cargando base de datos del calendario...</span>
                  </div>
                ) : filteredData.length === 0 ? (
                  <div className="text-center py-16 text-purple-300/50">
                    No se encontraron registros que coincidan con la búsqueda.
                  </div>
                ) : (
                  <table className="calendar-table">
                    <thead>
                      <tr>
                        <th>Libro / Serie</th>
                        <th>Cap</th>
                        <th>Título del Mensaje</th>
                        <th>Fecha Pub</th>
                        <th>Estado</th>
                        <th>Acción</th>
                      </tr>
                    </thead>
                    <tbody>
                      {filteredData.map(row => (
                        <tr 
                          key={row.id} 
                          onClick={() => loadRowContent(row)}
                          className={`cursor-pointer ${selectedRow?.id === row.id ? 'bg-purple-950/20 border-l-4 border-purple-500' : ''}`}
                        >
                          <td className="font-bold text-white text-sm max-w-[130px] truncate">{row.Libro}</td>
                          <td className="text-purple-300 font-semibold">{row.Capitulo}</td>
                          <td className="text-purple-100 max-w-[200px] truncate">{row.Titulo}</td>
                          <td className="text-purple-300 text-xs font-mono">{row.Fecha_Publicacion || 'Sin Fecha'}</td>
                          <td>
                            <span className={`badge ${
                              row.Estado?.toLowerCase() === 'publicado' ? 'badge-publicado' :
                              row.Estado?.toLowerCase() === 'pendiente' ? 'badge-pendiente' : 'badge-draft'
                            }`}>
                              {row.Estado || 'Draft'}
                            </span>
                          </td>
                          <td>
                            <button className="text-purple-400 hover:text-white p-1 transition-all">
                              <ChevronRight className="w-5 h-5" />
                            </button>
                          </td>
                        </tr>
                      ))}
                    </tbody>
                  </table>
                )}
              </div>

              {/* Detailed View / Editor Panel */}
              <div className="glass-card p-6 flex flex-col min-h-[600px] relative">
                {selectedRow ? (
                  <div className="flex flex-col h-full animate-in fade-in duration-300">
                    
                    {/* Header Details Panel */}
                    <div className="flex justify-between items-start border-b border-purple-950 pb-4 mb-4">
                      <div>
                        <span className="text-xs font-bold text-purple-400 uppercase tracking-widest">{selectedRow.Libro}</span>
                        <h3 className="text-xl font-bold text-white">Capítulo {selectedRow.Capitulo}: {selectedRow.Titulo}</h3>
                      </div>
                      <button 
                        onClick={() => setSelectedRow(null)}
                        className="text-purple-400 hover:text-white transition-all"
                      >
                        <X className="w-5 h-5" />
                      </button>
                    </div>

                    {loadingContent ? (
                      <div className="flex flex-col items-center justify-center py-20 gap-3 flex-1">
                        <Loader2 className="w-6 h-6 text-purple-500 animate-spin" />
                        <span className="text-xs text-purple-300/40">Cargando guiones de voz y posts...</span>
                      </div>
                    ) : (
                      <div className="flex-1 flex flex-col gap-4 overflow-y-auto max-h-[650px] pr-2">
                        
                        {/* Editor Form fields */}
                        <div className="grid grid-cols-2 gap-3 bg-purple-950/15 p-3 rounded-xl border border-purple-900/20">
                          <div className="flex flex-col">
                            <label className="text-[10px] font-bold text-purple-400 uppercase tracking-wider mb-1">Título Interfaz</label>
                            <input 
                              type="text" 
                              value={editFields.Titulo}
                              onChange={(e) => setEditFields(prev => ({ ...prev, Titulo: e.target.value }))}
                              className="form-input text-xs"
                            />
                          </div>

                          <div className="flex flex-col">
                            <label className="text-[10px] font-bold text-purple-400 uppercase tracking-wider mb-1">Fecha de Publicación</label>
                            <input 
                              type="text" 
                              value={editFields.Fecha_Publicacion}
                              onChange={(e) => setEditFields(prev => ({ ...prev, Fecha_Publicacion: e.target.value }))}
                              className="form-input text-xs font-mono"
                              placeholder="AAAA-MM-DD"
                            />
                          </div>

                          <div className="flex flex-col col-span-2">
                            <label className="text-[10px] font-bold text-purple-400 uppercase tracking-wider mb-1">Estado de Lanzamiento</label>
                            <select 
                              value={editFields.Estado}
                              onChange={(e) => setEditFields(prev => ({ ...prev, Estado: e.target.value }))}
                              className="form-input text-xs"
                            >
                              <option value="Draft">Draft (Borrador)</option>
                              <option value="pendiente">Pendiente (Programado)</option>
                              <option value="publicado">Publicado</option>
                            </select>
                          </div>
                        </div>

                        {/* Visual Asset Section */}
                        {detailContent.coverExists && (
                          <div className="bg-purple-950/20 border border-purple-900/30 rounded-xl p-3 flex items-center gap-3">
                            <div className="bg-purple-600/10 p-2.5 rounded-lg">
                              <ImageIcon className="w-5 h-5 text-purple-400" />
                            </div>
                            <div className="flex-1">
                              <div className="text-xs font-bold text-white">Portada Disponible</div>
                              <span className="text-[10px] font-mono text-purple-400">{detailContent.coverPath}</span>
                            </div>
                          </div>
                        )}

                        {/* Collapsible Content Panels */}
                        
                        {/* Tabbed Visor: Guion / Post */}
                        <div className="mt-2 border-t border-purple-950/40 pt-4">
                          <h4 className="text-xs font-bold text-purple-300 uppercase tracking-wider mb-2">📜 Guion de Voz en Off (Audio)</h4>
                          <div className="bg-purple-950/15 border border-purple-950/50 rounded-xl p-4 max-h-[250px] overflow-y-auto text-sm text-purple-200">
                            {renderMarkdown(detailContent.script)}
                          </div>
                        </div>

                        {/* Proposed Hook Titles */}
                        {detailContent.titles && (
                          <div className="mt-3 border-t border-purple-950/40 pt-3">
                            <h4 className="text-xs font-bold text-purple-300 uppercase tracking-wider mb-2">💡 Títulos Gancho Propuestos</h4>
                            <div className="bg-purple-950/15 border border-purple-950/50 rounded-xl p-4 max-h-[180px] overflow-y-auto text-sm text-purple-200">
                              {renderMarkdown(detailContent.titles)}
                            </div>
                          </div>
                        )}

                        <div className="mt-3 border-t border-purple-950/40 pt-3">
                          <div className="flex justify-between items-center mb-2">
                            <h4 className="text-xs font-bold text-purple-300 uppercase tracking-wider">📱 Post de Facebook Listo</h4>
                            
                            <button 
                              onClick={() => copyToClipboard(editFields.Texto_Post || detailContent.post)}
                              className={`flex items-center gap-1.5 px-2.5 py-1 rounded-lg text-xs font-bold transition-all ${
                                copySuccess 
                                  ? 'bg-emerald-500/20 text-emerald-400 border border-emerald-500/30 animate-pulse'
                                  : 'bg-purple-600/10 text-purple-300 hover:bg-purple-600/20 border border-purple-500/20'
                              }`}
                            >
                              {copySuccess ? <Check className="w-3.5 h-3.5" /> : <Copy className="w-3.5 h-3.5" />}
                              <span>{copySuccess ? 'Copiado!' : 'Copiar Post'}</span>
                            </button>
                          </div>
                          
                          <textarea
                            value={editFields.Texto_Post || detailContent.post}
                            onChange={(e) => setEditFields(prev => ({ ...prev, Texto_Post: e.target.value }))}
                            className="form-input w-full text-xs font-sans h-32 resize-none"
                            placeholder="Introduce el texto del post aquí..."
                          />
                        </div>

                        {/* Save Action Button */}
                        <button 
                          onClick={handleSaveRow}
                          disabled={savingRow}
                          className="btn-primary py-3 w-full mt-4 flex items-center justify-center gap-2"
                        >
                          {savingRow ? <Loader2 className="w-4 h-4 animate-spin" /> : <Save className="w-4 h-4" />}
                          <span>Guardar Cambios</span>
                        </button>

                      </div>
                    )}
                  </div>
                ) : (
                  <div className="flex-1 flex flex-col items-center justify-center text-center text-purple-300/40 p-4">
                    <CalendarIcon className="w-12 h-12 mb-3 text-purple-500/30" />
                    <p className="font-medium text-sm">Selecciona una fila del calendario para visualizar sus guiones, copiar textos e interactuar con su contenido.</p>
                  </div>
                )}
              </div>
            </div>
          </div>
        )}

        {/* ------------------ AGENT CHAT TAB ------------------ */}
        {activeTab === 'chat' && (
          <div className="animate-in fade-in slide-in-from-bottom-4 duration-500 h-[calc(100vh-100px)] flex flex-col">
            <header className="mb-4">
              <h2 className="text-3xl font-extrabold text-white tracking-tight flex items-center gap-3">
                <Sparkles className="w-8 h-8 text-purple-400" />
                <span>Conversa con el Agente</span>
              </h2>
              <p className="text-purple-300/60 mt-1">Pregúntame sugerencias de copys, pide adaptaciones de guiones de voz o crea nuevas ideas.</p>
            </header>

            {/* Chat Container */}
            <div className="glass-card flex-1 flex flex-col min-h-0 relative p-4 mb-4">
              
              {/* Message History Scroller */}
              <div className="flex-1 overflow-y-auto space-y-4 pr-2 mb-4 scroll-smooth">
                {chatMessages.map((msg, index) => (
                  <div key={index} className={`flex ${msg.role === 'user' ? 'justify-end' : 'justify-start'}`}>
                    <div className={msg.role === 'user' ? 'chat-bubble-user' : 'chat-bubble-agent'}>
                      <div className="text-sm font-semibold tracking-wide mb-1 text-[10px] text-purple-300 uppercase tracking-widest">
                        {msg.role === 'user' ? 'Tú' : 'Creador de Guiones Reflexivos'}
                      </div>
                      <div className="text-sm leading-relaxed prose prose-invert max-w-none">
                        {renderMarkdown(msg.content)}
                      </div>
                    </div>
                  </div>
                ))}
                
                {chatLoading && (
                  <div className="flex justify-start">
                    <div className="chat-bubble-agent flex items-center gap-2 py-3.5">
                      <div className="text-xs text-purple-300 flex items-center gap-2">
                        <Loader2 className="w-4 h-4 animate-spin text-purple-400" />
                        <span>El agente está redactando e inspirándose...</span>
                      </div>
                    </div>
                  </div>
                )}
                
                <div ref={chatEndRef} />
              </div>

              {/* Input Form Box */}
              <form onSubmit={handleSendMessage} className="flex gap-3 border-t border-purple-950/60 pt-4">
                <input 
                  type="text"
                  placeholder="Escribe tu mensaje o instrucciones para el agente (ej. 'Muéstrame el guion del cap 2')..."
                  value={chatInput}
                  onChange={(e) => setChatInput(e.target.value)}
                  disabled={chatLoading}
                  className="form-input flex-1 py-3 text-sm"
                />
                <button 
                  type="submit"
                  disabled={chatLoading || !chatInput.trim()}
                  className="btn-primary px-6"
                >
                  <Send className="w-4 h-4" />
                  <span>Enviar</span>
                </button>
              </form>
            </div>

            {/* Quick Action Suggestions Prompts */}
            <div className="flex flex-wrap gap-2.5">
              <button 
                onClick={() => setChatInput('Escribe un post de Facebook alternativo para el último capítulo procesado.')}
                className="bg-purple-950/30 border border-purple-900/30 hover:border-purple-500/30 px-3.5 py-1.5 rounded-full text-xs font-semibold text-purple-300 hover:text-white transition-all"
              >
                💡 Generar Post Alternativo
              </button>
              <button 
                onClick={() => setChatInput('Dame sugerencias de 5 títulos gancho que apelen al bienestar emocional para el Capítulo 18 de Hágase la Luz.')}
                className="bg-purple-950/30 border border-purple-900/30 hover:border-purple-500/30 px-3.5 py-1.5 rounded-full text-xs font-semibold text-purple-300 hover:text-white transition-all"
              >
                ✍️ Sugerencias de Títulos Gancho
              </button>
              <button 
                onClick={() => setChatInput('Explícame brevemente el objetivo y las enseñanzas prácticas del Capítulo 2 de "Hágase la Luz".')}
                className="bg-purple-950/30 border border-purple-900/30 hover:border-purple-500/30 px-3.5 py-1.5 rounded-full text-xs font-semibold text-purple-300 hover:text-white transition-all"
              >
                📖 Resumen de Enseñanzas Cap 2
              </button>
            </div>
          </div>
        )}

      </main>
    </div>
  );
}
