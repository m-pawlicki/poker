import { useState, useEffect } from 'react';
import './App.css';
import * as Page from './Page';
import * as Game from './Game';

export default function App() {

   const [cardPicked, setCardPicked] = useState(null);

  return (
    <>
      <div className="parent">
        <div className="div-top">
          <Page.Header />
        </div>
        <div className="div-left">
          <Page.Menu />
        </div>
        <div className="div-mid">
          <Game.Table />
          <Game.Hand />
          <Page.Footer />
        </div>
        <div className="div-right">
          <Page.Info />
        </div>
      </div>
    </>
  )
}
