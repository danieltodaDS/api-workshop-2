import pytest

# Funciona com um servidor de teste
from fastapi.testclient import TestClient

from app.main import app 

client = TestClient(app)

def test_ola_mundo():
    response = client.get("/")
    assert response.status_code == 200 

def test_ola_mundo_json(): 
    response = client.get("/")
    
    assert response.json() == {"ola":"mundo"}

def test_lista_produtos_status_code(): 
    response = client.get("/produtos")

    assert response.status_code == 200

