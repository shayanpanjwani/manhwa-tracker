import { useState, useEffect } from "react";
import "./App.css";

function App() {
  const [message, setMessage] = useState("Loading...");

  useEffect(() => {
    fetch("http://localhost:8000")
      .then((res) => res.json())
      .then((data) => setMessage(data.message))
      .catch((err) => setMessage("Error connecting to the backend"));
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <h1>Manhwa Tracker</h1>
        <p>{message}</p>
      </header>
    </div>
  );
}

export default App;
