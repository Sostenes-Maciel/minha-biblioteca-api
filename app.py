# app.py (versão atualizada)
from flask import Flask, jsonify, request # Adicionado 'request'

app = Flask(__name__)

livros = [
    { 'id': 1, 'titulo': 'O Senhor dos Anéis', 'autor': 'J.R.R. Tolkien' },
    { 'id': 2, 'titulo': 'Duna', 'autor': 'Frank Herbert' },
    { 'id': 3, 'titulo': '1984', 'autor': 'George Orwell' }
]

@app.route('/api/livros', methods=['GET'])
def obter_livros():
    return jsonify(livros)

# Nova rota POST
@app.route('/api/livros', methods=['POST'])
def adicionar_livro():
    novo_livro = request.get_json()
    novo_livro['id'] = len(livros) + 1
    livros.append(novo_livro)
    return jsonify(novo_livro), 201

if __name__ == '__main__':
    app.run(debug=True, port=8080)