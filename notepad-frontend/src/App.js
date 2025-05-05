import React, { useState, useEffect } from 'react';
import './App.css';
import api from './api';
import NoteForm from './components/NoteForm';
import NoteList from './components/NoteList';
import LoginPage from './components/LoginPage';

function App() {
  const [notes, setNotes] = useState([]);
  const [selectedNote, setSelectedNote] = useState(null);
  const [isAuthenticated, setIsAuthenticated] = useState(!!localStorage.getItem('access_token'));

  const fetchNotes = async () => {
    try {
      const response = await api.get('/notes/');
      setNotes(response.data);
    } catch (error) {
      console.error('Failed to fetch notes:', error);
    }
  };

  useEffect(() => {
    if (isAuthenticated) {
      fetchNotes();
    }
  }, [isAuthenticated]);

  const addNote = async (note) => {
    try {
      await api.post('/notes/', note);
      fetchNotes();
    } catch (error) {
      console.error('Failed to add note:', error);
    }
  };

  const updateNote = async (id, updatedNote) => {
    try {
      await api.put(`/notes/${id}`, updatedNote);
      fetchNotes();
    } catch (error) {
      console.error('Failed to update note:', error);
    }
  };

  const deleteNote = async (id) => {
    try {
      await api.delete(`/notes/${id}`);
      fetchNotes();
    } catch (error) {
      console.error('Failed to delete note:', error);
    }
  };

  const selectNote = (note) => {
    setSelectedNote(note);
  };

  const clearSelection = () => {
    setSelectedNote(null);
  };

  const handleLogout = () => {
    localStorage.removeItem('access_token');
    setIsAuthenticated(false);
  };

  const handleLogin = () => {
    setIsAuthenticated(true);
  };

  if (!isAuthenticated) {
    return <LoginPage onLogin={handleLogin} />;
  }

  return (
    <div className="App">
      <header className="app-header">
        <h1>Notepad Application</h1>
        <button className="logout-btn" onClick={handleLogout}>Logout</button>
      </header>
      <NoteForm
        addNote={addNote}
        selectedNote={selectedNote}
        updateNote={updateNote}
        clearSelection={clearSelection}
      />
      <NoteList notes={notes} deleteNote={deleteNote} selectNote={selectNote} />
    </div>
  );
}

export default App;