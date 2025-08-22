import React, { useEffect } from "react";

const TabMonitor = () => {
  useEffect(() => {
    const handleVisibilityChange = () => {
      if (document.hidden) {
        alert("⚠️ You switched tabs! Please return to the test.");
      }
    };

    const handleBlur = () => {
      console.log("⚠️ Window lost focus (maybe switched apps).");
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

  return null; 
};

export default TabMonitor;
