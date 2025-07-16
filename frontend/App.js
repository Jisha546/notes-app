import React, { useState, useEffect } from "react";
import axios from "axios";

function App() {
  const [items, setItems] = useState([]);
  const [newName, setNewName] = useState("");
  const [newId, setNewId] = useState("");

  const fetchItems = () => {
    axios.get("http://127.0.0.1:8000/items")
      .then(res => setItems(res.data))
      .catch(err => console.error(err));
  };

  const addItem = () => {
    axios.post(`http://127.0.0.1:8000/items/${newId}?name=${newName}`)
      .then(fetchItems)
      .catch(err => console.error(err));
  };

  const updateItem = (id) => {
    const name = prompt("Enter new name:");
    axios.put(`http://127.0.0.1:8000/items/${id}?name=${name}`)
      .then(fetchItems)
      .catch(err => console.error(err));
  };

  const deleteItem = (id) => {
    axios.delete(`http://127.0.0.1:8000/items/${id}`)
      .then(fetchItems)
      .catch(err => console.error(err));
  };

  useEffect(() => {
    fetchItems();
  }, []);

  return (
    <div className="App">
      <h1>React + FastAPI CRUD</h1>

      <input
        placeholder="ID"
        value={newId}
        onChange={(e) => setNewId(e.target.value)}
      />
      <input
        placeholder="Name"
        value={newName}
        onChange={(e) => setNewName(e.target.value)}
      />
      <button onClick={addItem}>Add Item</button>

      <ul>
        {items.map(item => (
          <li key={item.id}>
            {item.id}: {item.name} 
            <button onClick={() => updateItem(item.id)}>Edit</button>
            <button onClick={() => deleteItem(item.id)}>Delete</button>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;

