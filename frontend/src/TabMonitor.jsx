import React, { useEffect, useState } from "react";

const TabMonitor = () => {
  const [violations, setViolations] = useState(0);

  useEffect(() => {
    const handleVisibilityChange = () => {
      if (document.hidden) {
        setViolations((prev) => prev + 1);
        alert("⚠️ You switched tabs! Please return to the test.");
      }
    };

    const handleBlur = () => {
      console.log("⚠️ Window lost focus.");
    };

    const handleFocus = () => {
      console.log("✅ Window active again.");
    };

    document.addEventListener("visibilitychange", handleVisibilityChange);
    window.addEventListener("blur", handleBlur);
    window.addEventListener("focus", handleFocus);

    return () => {
      document.removeEventListener("visibilitychange", handleVisibilityChange);
      window.removeEventListener("blur", handleBlur);
      window.removeEventListener("focus", handleFocus);
    };
  }, []);

  return (
    <div>
      <p>Violations: {violations}</p>
    </div>
  );
};

export default TabMonitor;
