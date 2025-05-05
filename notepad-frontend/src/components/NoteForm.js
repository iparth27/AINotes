//notepad-frontend/src/NoteForm.js
import React, { useState, useEffect } from 'react';
import './NoteForm.css';

function NoteForm({ addNote, selectedNote, updateNote, clearSelection }) {
  const [title, setTitle] = useState('');
  const [content, setContent] = useState('');
  const [error, setError] = useState('');

  useEffect(() => {
    if (selectedNote) {
      setTitle(selectedNote.title);
      setContent(selectedNote.content);
    }
  }, [selectedNote]);

  const handleSubmit = (e) => {
    e.preventDefault();

    // Validation
    if (title.trim() === '') {
      setError('Title cannot be empty');
      return;
    }
    if (content.trim().length < 10) {
      setError('Content must be at least 10 characters');
      return;
    }

    setError('');

    if (selectedNote) {
      updateNote(selectedNote.id, { title, content });
      clearSelection();
    } else {
      addNote({ title, content });
    }

    setTitle('');
    setContent('');
  };

  return (
    <div className="note-form-container">
      <h2>{selectedNote ? 'Edit Note' : 'Add Note'}</h2>
      {error && <p className="error-message">{error}</p>}
      <form onSubmit={handleSubmit} className="note-form">
        <input
          type="text"
          placeholder="Title"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
          className="note-input"
        />
        <textarea
          placeholder="Content (at least 10 characters)"
          value={content}
          onChange={(e) => setContent(e.target.value)}
          rows="5"
          className="note-textarea"
        />
        <div className="form-actions">
          <button type="submit" className="submit-btn">
            {selectedNote ? 'Update' : 'Add'}
          </button>
          {selectedNote && (
            <button type="button" onClick={clearSelection} className="cancel-btn">
              Cancel
            </button>
          )}
        </div>
      </form>
    </div>
  );
}

export default NoteForm;