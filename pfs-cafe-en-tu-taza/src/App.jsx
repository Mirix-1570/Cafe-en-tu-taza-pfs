import { useState } from "react";
import reactLogo from "./assets/react.svg";
import viteLogo from "/vite.svg";
//import './App.css'
import NavBar from "./components/Everywere/NavBar/NavBar";

function App() {
  return (
    <>
      <div className="layout-container flex h-full grow flex-col">
      <NavBar />
      </div>
    </>
  );
}

export default App;
