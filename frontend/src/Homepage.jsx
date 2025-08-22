import React, { useState } from "react";
import CameraMic from "./CameraMic";
import "./HomePage.css"; // Import CSS
import TabMonitor from "./TabMonitor";
const Homepage = () => {
  const [testStarted, setTestStarted] = useState(false);
  const [error, setError] = useState("");

  const startTest = async () => {
    try {
      await navigator.mediaDevices.getUserMedia({ video: true, audio: true });
      setTestStarted(true);
      setError("");
    } catch (err) {
      setError("You must allow webcam & mic to start the test.");
    }
  };

  const userName = "XYZ"; 
  const testName = "Mid-Term Exam";
  const subjectName = "Mathematics";

  return (
    <div className="homepage-container">
      {!testStarted ? (
        <>
          {/* Navbar */}
          <nav className="navbar">
            <div className="navbar-left">
              <span className="brand">Test Platform</span>
            </div>
            <div className="navbar-right">
              <a href="/">Home</a>
              <a href="/summary">Tests Summary</a>
              <a href="/logout">Logout</a>
              <span className="greeting">Hi, {userName}</span>
            </div>
          </nav>

          {/* Test Info Card */}
          <div className="test-card">
            <h2>{testName}</h2>
            <p><strong>Subject:</strong> {subjectName}</p>
            <button className="start-button" onClick={startTest}>Start Test</button>
            {error && <p className="error-text">{error}</p>}
          </div>
        </>
      ) : (
        <>
         <CameraMic />
         <TabMonitor/>
        </>
       
        
    
      )}
    </div>
  );
};

export default Homepage;
