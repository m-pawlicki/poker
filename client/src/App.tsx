import { useState, useEffect } from 'react';
import './App.css';

// A single card
function Card({value}) {
  return (
    <>
    <div className="card-container">
      <div className="card">
        <input type="radio" name="card" className="card-input" id={value} value={value}></input>
        <label className="card-face" htmlFor={value}>{value}</label>
      </div>
    </div>
    </>
  )

}

// A user's hand of cards
function Hand() {
  return (
    <>
    <div className="hand-container">
      <div className="card-hand">
        <Card value={"0"} />
        <Card value={"1"} />
        <Card value={"2"} />
        <Card value={"3"} />
        <Card value={"5"} />
        <Card value={"8"} />
        <Card value={"13"} />
        <Card value={"?"} />
        <Card value={"☕"} />
      </div>
    </div>
    </>
  )
}

// Visual representation of cards picked by users and the current story to vote upon
function Table() {
  return (
    <>
    <div className="story-container">
      <span><h3>Current Story: </h3><p id="current-story">Test</p></span>
    </div>
    <div className="table-container">
      <svg className="table" width="300" height="150">
        <rect width="300" height="150" rx="15" ry="15" fill="grey" />
      </svg>
    </div>
    </>
  )
}

// Header
function Header() {
  return (
    <>
    <div className="head-div">
      <header>
      <h1>Planning Poker</h1>
      </header>
    </div>
    </>
  )
}

// Footer
function Footer() {
  return (
    <>
    <div className="foot-div">
      <footer>
      <sub>Made with <i class="fa-solid fa-heart" /> Micah Pawlicki 2026</sub>
      </footer>
    </div>
    </>
  )
}

// User menu
function Menu() {
  return (
    <>
    <div className="menu-div">
      <nav id="sidebar">
        <ul>
      <li><a className="nav-a" href="#"><span><i class="fa-solid fa-user" /> Name</span></a></li>
      <li><input type="checkbox" className="hidden-check" id="check" onClick={checkClicked}/><label htmlFor="check"><a className="nav-a" href="#"><span id="icon"><i class="fa-solid fa-binoculars"></i></span><span id="text"> Watch</span></a></label></li>
      <li><a className="nav-a" href="#" id="change-story" onClick={openStoryDrop}><span><i class="fa-solid fa-hashtag" /> Story</span></a></li>
      <li><div className="story-toggle" id="story-toggle"><input type="text" className="story-input" id="story-input" name="story-input" /><input type="button" className="story-button" value="Change Story" onClick={changeStory}/></div></li>
      <li><a className="nav-a" href="#"><span><i class="fa-solid fa-wand-magic-sparkles" /> Reveal</span></a></li>
      <li><a className="nav-a" href="#"><span><i class="fa-solid fa-arrow-rotate-right" /> Reset</span></a></li>
      <li><a className="nav-a" href="#"><span><i class="fa-solid fa-share" /> Share</span></a></li>
      </ul>
      </nav>
    </div>
    </>
  )
}

function checkClicked() {
    let checkBox = document.getElementById("check");
    let icon = document.getElementById("icon");
    let text = document.getElementById("text");

    checkBox?.addEventListener("change", function() {
      if (this.checked) {
        icon.innerHTML = "<i class='fa-solid fa-users' />";
        text.innerHTML = " Join";
      } else {
        icon.innerHTML = "<i class='fa-solid fa-binoculars' />";
        text.innerHTML = " Watch";
      }
    });
}

function openStoryDrop() {
  let storyMenu = document.getElementById("story-toggle");
  if (storyMenu.style.display == "none") {
        storyMenu.style.display = "block"; // Show content
    } else {
        storyMenu.style.display = "none"; // Hide content
    };
}

function changeStory() {
  let field = document.getElementById("story-input");
  let input = field.value;
  let story = document.getElementById("current-story");
  story.innerHTML = input;
}

// Shows voting status and results
function Info() {
  return (
    <>
    <div className="info-div">
      <span><i class="fa-solid fa-star" /> <h3>Most picked</h3></span><br />
      <span><i class="fa-solid fa-bolt" /> <h3>Average</h3></span><br />
      <span><i class="fa-solid fa-chart-simple" /> <h3>Breakdown</h3></span>
    </div>
    </>
  )
}

export default function App() {

   const [cardPicked, setCardPicked] = useState(null);

  return (
    <>
      <div className="parent">
        <div className="div-top">
          <Header />
        </div>
        <div className="div-left">
          <Menu />
        </div>
        <div className="div-mid">
          <Table />
          <Hand />
          <Footer />
        </div>
        <div className="div-right">
          <Info />
        </div>
      </div>
    </>
  )
}
