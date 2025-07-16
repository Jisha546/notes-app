import React, { useState, useEffect } from 'react';
import axios from 'axios';

function App() {
  const [notes, setNotes] = useState([]);
  const [newNote, setNewNote] = useState('');

  useEffect(() => {
    fetchNotes();
  }, []);

  const fetchNotes = async () => {
    const res = await axios.get('http://127.0.0.1:8000/notes');
    setNotes(res.data);
  };

  const addNote = async () => {
    if (!newNote.trim()) return;
    await axios.post('http://127.0.0.1:8000/notes', { content: newNote });
    setNewNote('');
    fetchNotes();
  };

  const deleteNote = async (index) => {
    await axios.delete(`http://127.0.0.1:8000/notes/${index}`);
    fetchNotes();
  };

  return (
    <div style={{ padding: 20 }}>
      <h1>📝 Notes App</h1>
      <input
        type="text"
        value={newNote}
        onChange={(e) => setNewNote(e.target.value)}
        placeholder="Write a note..."
      />
      <button onClick={addNote}>Add Note</button>

      <ul>
        {notes.map((note, index) => (
          <li key={index}>
            {note.content}
            <button onClick={() => deleteNote(index)}>❌</button>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;
