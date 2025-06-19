import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import app
import pytest


@pytest.fixture
def klient():
    app.testing = True
    return app.test_client()

def test_dodawanie(klient):
    r = klient.post("/api/oblicz", json={"wyrazenie": "2+2"})
    assert r.status_code == 200
    assert r.json["wynik"] == 4

def test_potegowanie(klient):
    r = klient.post("/api/oblicz", json={"wyrazenie": "2^3"})
    assert r.status_code == 200
    assert r.json["wynik"] == 8

def test_pierwiastek(klient):
    r = klient.post("/api/oblicz", json={"wyrazenie": "√9"})
    assert r.status_code == 200
    assert r.json["wynik"] == 3

def test_dzielenie_przez_zero(klient):
    r = klient.post("/api/oblicz", json={"wyrazenie": "1/0"})
    assert r.status_code == 400
    assert "blad" in r.json
