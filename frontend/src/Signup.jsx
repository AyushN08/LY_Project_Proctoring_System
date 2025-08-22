import React, { useState } from "react";
import Homepage from "./Homepage";
import "./Signup.css"; // import CSS file

const Signup = () => {
  const [signedUp, setSignedUp] = useState(false);

  const handleSignup = (e) => {
    e.preventDefault();
    setSignedUp(true); 
  };

  if (signedUp) {
    return <Homepage />; 
  }

  return (
    <div className="signup-container">
      <form className="signup-form" onSubmit={handleSignup}>
        <h2>Create Account</h2>
        <input type="text" placeholder="Username" required />
        <input type="email" placeholder="Email" required />
        <input type="password" placeholder="Password" required />
        <button type="submit">Sign Up</button>
      </form>
    </div>
  );
};

export default Signup;


