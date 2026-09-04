from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Team Practice API")

# Allow frontend to communicate with backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class EmailRequest(BaseModel):
    email: str


@app.get("/")
def home():
    return {"message": "Backend is working!"}


@app.post("/analyze")
def analyze_email(data: EmailRequest):

    email = data.email.lower()

    if "urgent" in email or "password" in email or "verify" in email:
        classification = "PHISHING"
        risk_score = 90
        reason = "Suspicious words detected"
    else:
        classification = "SAFE"
        risk_score = 10
        reason = "No major threat detected"

    return {
        "classification": classification,
        "risk_score": risk_score,
        "reason": reason
    }