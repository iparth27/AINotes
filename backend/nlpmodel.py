#backend/nlpmodel.py
from textblob import TextBlob

threshold_pos = 0.1
threshold_neg = -0.1


def analyze_sentiment(text: str) -> str:
    """
    Analyzes the sentiment of the input text.

    Returns:
        'positive', 'neutral', or 'negative'
    """
    if not text.strip():
        return "neutral"  # Default for empty input

    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    if polarity >= threshold_pos:
        return "positive"
    elif polarity <= threshold_neg:
        return "negative"
    else:
        return "neutral"