"use strict";

function Homepage() {
  return (
    <React.Fragment>
      <h1>Hello and Welcome to the Trading Cards World!</h1>
      <a href="/cards">Navigate me to a Cards Page</a>
      <img src="/static/img/balloonicorn.jpg"></img>
    </React.Fragment>
  );
}

ReactDOM.render(<Homepage />, document.querySelector('#app'));
