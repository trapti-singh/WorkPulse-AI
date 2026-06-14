from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "project": "WorkPulse AI",
        "status": "Prototype"
    }
