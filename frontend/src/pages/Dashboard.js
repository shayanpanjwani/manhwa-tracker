import { useState, useEffect } from "react";
import "../App.css";

function Dashboard() {
  const [series, setSeries] = useState([]);

  const [loading, setLoading] = useState(false);

  useEffect(() => {
    setLoading(true);
    fetch("http://localhost:8000/api/series")
      .then((res) => res.json())
      .then((data) => {
        setSeries(data);
        setLoading(false);
      })
      .catch((err) => {
        console.error(err);
        setLoading(false);
      });
  }, []);

  if (loading) {
    return <div>Loading...</div>;
  }

  return (
    <div className="dashboard">
      <h1>My Manhwa Collection</h1>
      {series.map((s) => (
        <div key={s.id} className="series-card">
          <h3>{s.title}</h3>
          <p>
            Reading Progress: {s.current_chapter} / {s.total_chapters_available}
          </p>
          <p> Rating: {s.rating ? "⭐".repeat(s.rating) : "Not rated"} </p>
          <a href={s.aggregator_url} target="_blank" rel="noopener noreferrer">
            Read on MangaRead
          </a>
        </div>
      ))}
    </div>
  );
}

export default Dashboard;
