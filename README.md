# API de Biblioteca

Esta é uma API REST simples para gerenciar uma coleção de livros.

## Workflow de Desenvolvimento

O workflow adotado foi o **GitHub Flow** por seu equilíbrio ideal entre agilidade e segurança para este projeto. Diferente de modelos mais complexos como o Git Flow, que seria um exagero para esta escala, o GitHub Flow é simples e direto. Ele se baseia em uma regra fundamental: a branch main está sempre estável e funcional. Todo o desenvolvimento de novas funcionalidades acontece em feature branches separadas, o que garante que o código principal nunca seja quebrado e organiza o histórico de forma clara, onde cada merge na main representa a adição de uma funcionalidade completa e testada.
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