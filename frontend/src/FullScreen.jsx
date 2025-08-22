import React,{useEffect} from "react";




  
const FullscreenButton = () => {
  const goFullscreen = () => {
    const elem = document.documentElement; // whole page
    if (elem.requestFullscreen) {
      elem.requestFullscreen();
    } else if (elem.webkitRequestFullscreen) { // Safari
      elem.webkitRequestFullscreen();
    } else if (elem.msRequestFullscreen) { // IE/Edge
      elem.msRequestFullscreen();
    }
  };
  useEffect(() => {
    const handleFullscreenChange = () => {
      if (!document.fullscreenElement) {
        alert("⚠️ You exited fullscreen! Please return to the test.");
      }
    };
  
    document.addEventListener("fullscreenchange", handleFullscreenChange);
  
    return () => {
      document.removeEventListener("fullscreenchange", handleFullscreenChange);
    };
  }, []);

  return (
    <button onClick={goFullscreen}>
      Start Test in Fullscreen
    </button>
  );
};

export default FullscreenButton;
