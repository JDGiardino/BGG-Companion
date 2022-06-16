import React, { useEffect, useState} from 'react';
import './App.css';
type GameT = {
  description: string;
  id: number;
  image: string;
  maxplayers: number;
  minplayers: number;
  name: string;
  thumbnail: string;
  type: string;
}
function App() {
  const [randomGame, setRandomGame] = useState<GameT | undefined>()
  useEffect(() => {
    fetch('/random_game?user=JDGiardino').then(response => response.json())
    .then(data => {
      console.log(data);
      setRandomGame(data);
    })
  }, [])

  return (
    <div className="App">
      <div>
        BGG
      </div>
      {randomGame && (<div>{randomGame.name}</div>) }
    </div>
  );
}

export default App;
