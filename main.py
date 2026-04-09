from fastapi import FastAPI
from model import analyze_text
from schemas import TextRequest

app = FastAPI()

# Home route
@app.get("/")
def home():
    return {"message": "Sentiment Analysis API is running 🚀"}


# Health check
@app.get("/health")
def health():
    return {"status": "OK"}


# Sentiment API
@app.post("/analyze")
def analyze(request: TextRequest):
    text = request.text

    # Validation
    if not text or not text.strip():
        return {"error": "Text cannot be empty"}

    # Model result
    result = analyze_text(text)

    label = result["label"]
    score = result["score"]

    # ✅ Correct NEUTRAL logic
    if score < 0.85:
        label = "NEUTRAL"

    return {
        "label": label,
        "confidence": round(score, 3)
    }