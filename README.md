# API de Biblioteca

Esta é uma API REST simples para gerenciar uma coleção de livros.

## Workflow de Desenvolvimento

Este projeto utiliza o **GitHub Flow**. O motivo da escolha foi sua simplicidade e segurança, mantendo a branch `main` sempre estável.

## Como Executar

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/Sostenes-Maciel/minha-biblioteca-api.git](https://github.com/Sostenes-Maciel/minha-biblioteca-api.git)
    cd minha-biblioteca-api
    ```
2.  ... (instruções de ambiente e instalação) ...
3.  Execute: `python app.py`

## Rotas Disponíveis

### 1. Obter todos os livros
- **Método:** `GET`
- **URL:** `/api/livros`

### 2. Adicionar um novo livro
- **Método:** `POST`
- **URL:** `/api/livros`
- **Corpo da Requisição:**
  ```json
  {
      "titulo": "Neuromancer",
      "autor": "William Gibson"
  }
  ```