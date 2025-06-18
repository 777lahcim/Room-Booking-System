import React, { useEffect, useState } from 'react';

interface Room {
  id: number;
  name: string;
  capacity: number;
}

function App() {
  const [rooms, setRooms] = useState<Room[]>([]);

  useEffect(() => {
    fetch('http://localhost:8000/api/rooms/')
      .then(res => res.json())
      .then(data => setRooms(data));
  }, []);

  return (
    <div>
      <h1>Lista pokoi</h1>
      <ul>
        {rooms.map(room => (
          <li key={room.id}>
            {room.name} — pojemność: {room.capacity}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;
