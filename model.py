from transformers import pipeline

# Load model once (important for performance)
sentiment_pipeline = pipeline("sentiment-analysis")

def analyze_text(text: str):
    result = sentiment_pipeline(text)
    return result[0]   # return first result