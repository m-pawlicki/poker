// A single card
export function Card({value}) {
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
export function Hand() {
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
export function Table() {
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