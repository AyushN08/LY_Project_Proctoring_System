from fastapi import FastAPI
from fastapi.responses import JSONResponse
import subprocess
import os
from fastapi.middleware.cors import CORSMiddleware
import sys
app = FastAPI()

# ✅ Add middleware after app creation
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

process = None  # global reference to proctoring process

@app.post("/api/start-proctoring")
def start_proctoring():
    global process
    if process is None:
        process = subprocess.Popen([sys.executable, "proctoring_agent.py"])
        return {"status": "Proctoring started"}
    return {"status": "Already running"}

@app.post("/api/stop-proctoring")
def stop_proctoring():
    global process
    if process:
        process.terminate()
        process = None
        return {"status": "Proctoring stopped"}
    return {"status": "Not running"}

@app.get("/api/logs")
def get_logs():
    if os.path.exists("exam_logs.json"):
        with open("exam_logs.json", "r") as f:
            logs = f.readlines()
        return JSONResponse(content={"logs": [l.strip() for l in logs]})
    return {"logs": []}
