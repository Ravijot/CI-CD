from fastapi.testclient import TestClient
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app.main import myapp  # Import the FastAPI app from main.py

client = TestClient(myapp)

def test_read_root():
    response = client.get("/check")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to FastAPI"}  # Adjust based on your root endpoint response
