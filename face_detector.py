import cv2
import mediapipe as mp
import random
import os
import time
from datetime import datetime

class FaceDetector:
    def __init__(self, logger, snapshot_dir="snapshots", user_folder="user1"):
        self.logger = logger
        self.snapshot_dir = snapshot_dir
        self.user_folder = os.path.join(snapshot_dir, user_folder)
        os.makedirs(self.user_folder, exist_ok=True)
        self.last_face_save_time = 0.0
        self.save_interval = random.uniform(3.0, 5.0)
        self.mp_face_detection = mp.solutions.face_detection

    def detect_faces(self, frame, detector):
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = detector.process(rgb)
        return result.detections if result and result.detections else []

    def process_frame(self, frame, detector):
        detections = self.detect_faces(frame, detector)
        face_count = len(detections)
        face_bboxes = []
        face_images = []
        h, w, _ = frame.shape
        for det in detections:
            if not det.location_data or not det.location_data.relative_bounding_box:
                continue
            bboxC = det.location_data.relative_bounding_box
            x1 = max(int(bboxC.xmin * w), 0)
            y1 = max(int(bboxC.ymin * h), 0)
            x2 = min(int((bboxC.xmin + bboxC.width) * w), w - 1)
            y2 = min(int((bboxC.ymin + bboxC.height) * h), h - 1)
            if x2 <= x1 or y2 <= y1:
                continue
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            face_bboxes.append({"x1": x1, "y1": y1, "x2": x2, "y2": y2})
            face_crop = frame[y1:y2, x1:x2]
            if face_crop.size > 0:
                face_images.append(face_crop)
        cv2.putText(frame, f"Faces detected: {face_count}", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        # Save snapshot if needed
        current_time = time.time()
        if face_images and (current_time - self.last_face_save_time >= self.save_interval):
            timestamp_str = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
            face_image_path = os.path.join(self.user_folder, f"face_{timestamp_str}.jpg")
            try:
                cv2.imwrite(face_image_path, face_images[0])
                self.last_face_save_time = current_time
                self.save_interval = random.uniform(3.0, 5.0)
                self.logger.log_event("User activity snapshot", confidence=1.0,
                    snapshot={"face_count": face_count, "face_bboxes": face_bboxes, "face_image_path": face_image_path})
            except Exception as e:
                self.logger.log_event("snapshot_error", confidence=0.0, snapshot={"error": str(e)})
        # Log face presence
        if face_count == 0:
            self.logger.log_event("No face detected", confidence=0.0)
        elif face_count > 1:
            self.logger.log_event("Multiple faces detected", confidence=1.0)
        return frame
