// notepad-frontend/src/NoteList.py
import React from 'react';
import './NoteList.css';

function NoteList({ notes, deleteNote, selectNote }) {
  return (
    <div className="note-list">
      {notes.map((note) => (
        <div key={note.id} className="note-card">
          <div className="note-content">
            <h3>{note.title}</h3>
            <p>{note.content}</p>
            <p>
              <strong>Sentiment:</strong> {note.sentiment}
            </p>
          </div>
          <div className="note-actions">
              <button className="edit-button" onClick={() => selectNote(note)}>Edit</button>
              <button className="delete-button" onClick={() => deleteNote(note.id)}>Delete</button>
          </div>
        </div>
      ))}
    </div>
  );
}

export default NoteList;
