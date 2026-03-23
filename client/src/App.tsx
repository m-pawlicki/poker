import { useState, useEffect } from 'react'
import './App.css'

function App() {
  const [room, setRoom] = useState(null)

  useEffect(() => {
    fetch('api/room')
    .then(res => res.json())
    .then(data => {
      setRoom(data);
    });
  }, []);

  return (
    <>
      <section id="center">
        <div>
          <h1>Planning Poker</h1>
          <p>
            Create Room | Join Room
          </p>
        </div>
        <button
          className="counter"
          onClick={() => setRoom(room)}
        >
          Get Rooms
        </button>
        {JSON.stringify(room) ? JSON.stringify(room): 'Active room(s)...'}
      </section>
    </>
  )
}

export default App
