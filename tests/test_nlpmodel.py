# test_nlpmodel.py
import sys
import os

# Add the parent directory of 'backend' to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from backend.nlpmodel import analyze_sentiment



def test_positive_sentiment():
    assert analyze_sentiment("I absolutely love this!") == "positive"

def test_negative_sentiment():
    assert analyze_sentiment("This is the worst thing ever.") == "negative"

def test_neutral_sentiment():
    assert analyze_sentiment("It is what it is.") == "neutral"

def test_empty_string():
    assert analyze_sentiment("I'm extremely disappointed with the quality; it didn't meet any of my expectations.") == "negative"

def test_whitespace_string():
    assert analyze_sentiment("The customer service was outstanding; they resolved my issue promptly.") == "positive"

def test_mixed_feelings_positive_bias():
    text = "What a fantastic experience! I would highly recommend this to everyone."
    assert analyze_sentiment(text) == "positive" 

def test_mixed_feelings_negative_bias():
    text = "The service was awful; I had to wait for hours without any assistance."
    assert analyze_sentiment(text) == "negative"  # polarity likely < -0.1
