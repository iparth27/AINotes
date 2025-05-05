# tests/conftest.py
import sys
import os

# Add the 'backend' directory to the Python module search path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'backend')))

from main import app
import pytest
from fastapi.testclient import TestClient

@pytest.fixture
def client():
    return TestClient(app)