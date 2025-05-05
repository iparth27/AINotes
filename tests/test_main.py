# tests/test_api.py
import sys
import os

# Add the parent directory of 'backend' to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# tests/test_main.py
import pytest
from fastapi.testclient import TestClient
from backend.main import app  # Adjust the import based on your project structure

client = TestClient(app)

@pytest.fixture
def test_user():
    res = client.post("/token/", data={"username": "testuser", "password": "testpass"})
    assert res.status_code == 200
    return {"username": "testuser", "password": "testpass"}

@pytest.fixture
def auth_token(test_user):
    res = client.post("/token", data={
        "username": test_user["username"],
        "password": test_user["password"]
    })
    assert res.status_code == 200
    return res.json()["access_token"]

def test_create_note(auth_token):
    response = client.post("/notes/", 
        json={"title": "Test Title", "content": "This is amazing!"},
        headers={"Authorization": f"Bearer {auth_token}"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["sentiment"] == "positive"

def test_get_notes(auth_token):
    response = client.get("/notes/", headers={"Authorization": f"Bearer {auth_token}"})
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_update_note(auth_token):
    create = client.post("/notes/", 
        json={"title": "Update Me", "content": "Will be updated"},
        headers={"Authorization": f"Bearer {auth_token}"}
    )
    note_id = create.json()["id"]
    response = client.put(f"/notes/{note_id}", 
        json={"title": "Updated", "content": "Now this is great!"},
        headers={"Authorization": f"Bearer {auth_token}"}
    )
    assert response.status_code == 200
    assert response.json()["title"] == "Updated"

def test_delete_note(auth_token):
    create = client.post("/notes/", 
        json={"title": "Delete Me", "content": "Please delete"},
        headers={"Authorization": f"Bearer {auth_token}"}
    )
    note_id = create.json()["id"]
    response = client.delete(f"/notes/{note_id}", headers={"Authorization": f"Bearer {auth_token}"})
    assert response.status_code == 200
    assert response.json()["message"] == "Note deleted successfully"
