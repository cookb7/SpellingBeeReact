import './App.css';
import React from 'react';
import Input from './Components/input';


function App() {
  return (
    <div className="App">
      <h1>Spelling Bee </h1>
      <div>
        Enter the letters for the Spelling Bee you would like to solve. Enter each letter with a space between them. Enter the primary letter last.
      </div>
      
      <div className="text-input-container"> {/* Apply CSS class to the text input container */}
        <Input/>
      </div>
    </div>
  );
}

export default App;
