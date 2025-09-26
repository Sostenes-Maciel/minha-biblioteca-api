# tests/test_app.py
import pytest
from app import app # Importa nossa aplicação Flask do arquivo app.py

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_obter_livros(client):
    """Testa se a rota GET /api/livros retorna o status 200 OK."""
    response = client.get('/api/livros')
    assert response.status_code == 200
    assert isinstance(response.json, list) # Verifica se a resposta é uma lista