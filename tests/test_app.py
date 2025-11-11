import pytest
import copy
from app import app

LIVROS_INICIAIS = [
    {"id": 1, "titulo": "O Senhor dos Anéis", "autor": "J.R.R. Tolkien"},
    {"id": 2, "titulo": "Duna", "autor": "Frank Herbert"},
    {"id": 3, "titulo": "1984", "autor": "George Orwell"},
]


@pytest.fixture
def client():
    app.livros = copy.deepcopy(LIVROS_INICIAIS)
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_deletar_livro_sucesso(client):
    id_para_deletar = 1
    response = client.delete(f"/api/livros/{id_para_deletar}")
    assert response.status_code == 204
    assert response.data == b""
    livro_removido = next(
        (livro for livro in app.livros if livro["id"] == id_para_deletar), None
    )
    assert livro_removido is None
    assert len(app.livros) == len(LIVROS_INICIAIS) - 1


def test_deletar_livro_nao_encontrado(client):
    id_inexistente = 999
    response = client.delete(f"/api/livros/{id_inexistente}")
    assert response.status_code == 404
    assert len(app.livros) == len(LIVROS_INICIAIS)


def test_obter_livros(client):
    response = client.get("/api/livros")
    assert response.status_code == 200
    assert len(response.get_json()) == 3


def test_adicionar_livro(client):
    novo_livro_data = {"titulo": "Neuromancer", "autor": "William Gibson"}
    assert len(app.livros) == len(LIVROS_INICIAIS)
    response = client.post("/api/livros", json=novo_livro_data)
    assert response.status_code == 201
    json_data = response.get_json()
    assert json_data["titulo"] == "Neuromancer"
    assert json_data["id"] == len(LIVROS_INICIAIS) + 1
    assert len(app.livros) == len(LIVROS_INICIAIS) + 1


def test_atualizar_livro_sucesso(client):
    id_para_atualizar = 2
    dados_atualizados = {"titulo": "Duna: Parte Um"}
    response = client.put(f"/api/livros/{id_para_atualizar}", json=dados_atualizados)
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data["titulo"] == "Duna: Parte Um"


def test_atualizar_livro_nao_encontrado(client):
    id_inexistente = 999
    dados_atualizados = {"titulo": "Inexistente"}
    response = client.put(f"/api/livros/{id_inexistente}", json=dados_atualizados)
    assert response.status_code == 404
