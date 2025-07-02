import httpx
import pytest

BASE_URL = "http://localhost:3000"

@pytest.mark.integration
def test_docker_cotacao_dolar():
    response = httpx.get(f"{BASE_URL}/cotacao/dolar")
    assert response.status_code == 200
    data = response.json()
    assert data["currency_name"] == "dollar"

@pytest.mark.integration
def test_docker_cotacao_euro():
    response = httpx.get(f"{BASE_URL}/cotacao/euro")
    assert response.status_code == 200
    data = response.json()
    assert data["cotacao"]["moeda"] == "EURO"