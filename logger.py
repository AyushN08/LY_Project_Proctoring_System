import logging
import json
from datetime import datetime

class EventLogger:
    def __init__(self, log_path="exam_logs.json"):
        self.log_path = log_path
        logging.basicConfig(
            filename=self.log_path,
            level=logging.INFO,
            format="%(message)s"
        )

    def log_event(self, event_type, confidence=1.0, snapshot=None):
        event = {
            "time": datetime.now().isoformat(),
            "event_type": event_type,
            "confidence": confidence,
            "snapshot": snapshot
        }
        logging.info(json.dumps(event))
