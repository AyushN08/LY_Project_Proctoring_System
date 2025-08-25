# backend/proctoring_agent.py
from logger import EventLogger
from audio_monitor import AudioMonitor
from screen_monitor import ScreenMonitor
from face_detector import FaceDetector
import cv2
import time

def main():
    logger = EventLogger()
    audio_monitor = AudioMonitor(logger)
    screen_monitor = ScreenMonitor(logger)
    face_detector = FaceDetector(logger)

    audio_monitor.start()

    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        logger.log_event("webcam_error", confidence=0.0, snapshot="cannot open webcam")
        return

    with face_detector.mp_face_detection.FaceDetection(model_selection=0, min_detection_confidence=0.6) as detector:
        try:
            while True:
                ret, frame = cap.read()
                if not ret:
                    logger.log_event("webcam_error", confidence=0.0, snapshot="cannot read frame")
                    break

                frame = face_detector.process_frame(frame, detector)

                current_time = time.time()
                if int(current_time) % 10 == 0:
                    screen_info = screen_monitor.monitor_screen()
                    if screen_info:
                        logger.log_event("Screen Event", confidence=1.0, snapshot=screen_info)

                cv2.imshow("Exam Proctoring (press 'q' to quit)", frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    logger.log_event("session_ended_by_user", confidence=1.0)
                    break
        except KeyboardInterrupt:
            logger.log_event("session_interrupted", confidence=0.0)
        except Exception as e:
            logger.log_event("runtime_error", confidence=0.0, snapshot={"error": str(e)})
        finally:
            cap.release()
            cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
