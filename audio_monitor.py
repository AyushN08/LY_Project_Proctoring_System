import threading
import speech_recognition as sr

class AudioMonitor:
    def __init__(self, logger, talk_file="talking.user", rate=16000):
        self.logger = logger
        self.talk_file = talk_file
        self.rate = rate

    def continuous_speech_recognition(self):
        recognizer = sr.Recognizer()
        print("🎤 Continuous speech recognition started...")
        try:
            with sr.Microphone(sample_rate=self.rate) as source:
                while True:
                    try:
                        audio = recognizer.listen(source, phrase_time_limit=5)
                        try:
                            text = recognizer.recognize_google(audio)
                            with open(self.talk_file, "a", encoding="utf-8") as f:
                                f.write(text + "\n")
                            self.logger.log_event("User speech recognized", confidence=1.0, snapshot={"text": text})
                        except sr.UnknownValueError:
                            pass
                        except Exception as e:
                            self.logger.log_event("speech_recognition_error", confidence=0.0, snapshot={"error": str(e)})
                    except Exception as e:
                        self.logger.log_event("mic_error", confidence=0.0, snapshot={"error": str(e)})
        except Exception as e:
            self.logger.log_event("mic_error", confidence=0.0, snapshot={"error": str(e)})

    def start(self):
        t = threading.Thread(target=self.continuous_speech_recognition, daemon=True)
        t.start()
