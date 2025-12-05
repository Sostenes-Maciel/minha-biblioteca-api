📚 Minha Biblioteca API



📦 Imagem Docker

A imagem oficial deste projeto está disponível no Docker Hub:

👉 https://hub.docker.com/r/sosthe09/minha-biblioteca-api

🔧 Como baixar a imagem
```bash
docker pull sosthe09/minha-biblioteca-api:latest
```
🚀 Workflow de Desenvolvimento

O workflow adotado foi o GitHub Flow, por oferecer simplicidade e segurança.
A branch main se mantém sempre estável, enquanto novas features são desenvolvidas em branches próprias e só são mescladas após revisadas e testadas.

🚀 Como Executar Localmente

Clone o repositório:
```bash
git clone https://github.com/Sostenes-Maciel/minha-biblioteca-api.git
cd minha-biblioteca-api
```

Instale dependências e configure o ambiente

Execute:
```bash
python app.py
```
📡 Rotas Disponíveis

Todas as rotas da API estão listadas abaixo:
```bash
# 1. Obter todos os livros
GET /api/livros

# 2. Adicionar um novo livro
POST /api/livros
Body:
{
    "titulo": "Neuromancer",
    "autor": "William Gibson"
}

# 3. Deletar um livro pelo ID
DELETE /api/livros/<id>
Exemplo:
DELETE /api/livros/3
```
