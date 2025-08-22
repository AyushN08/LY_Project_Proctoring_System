import React, { useEffect, useRef } from "react";

const CameraMic = () => {
  const videoRef = useRef(null);

  useEffect(() => {
    async function enableStream() {
      try {
        const stream = await navigator.mediaDevices.getUserMedia({
          video: true,
          audio: true,
        });
        if (videoRef.current) {
          videoRef.current.srcObject = stream;
        }
      } catch (err) {
        console.error("Error accessing camera/microphone:", err);
      }
    }
    enableStream();
  }, []);

  return (
    <div>
      <h2>Exam in Progress...</h2>
      <video ref={videoRef} autoPlay playsInline width="400" />
    </div>
  );
};

export default CameraMic;
