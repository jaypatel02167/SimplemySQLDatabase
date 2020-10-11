import React from 'react';
import logo from './logo.svg';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h2>Database</h2>
        <p>Username | User ID</p>
      <p>{window.token}</p>
      </header>
    </div>
  );
}

export default App;
