from flask import Flask, jsonify, request, Response

app = Flask(__name__)

# --- Base de dados de exemplo (associada ao app) ---
app.livros = [
    { 'id': 1, 'titulo': 'O Senhor dos Anéis', 'autor': 'J.R.R. Tolkien' },
    { 'id': 2, 'titulo': 'Duna', 'autor': 'Frank Herbert' },
    { 'id': 3, 'titulo': '1984', 'autor': 'George Orwell' }
]

# --- Rota GET para obter todos os livros ---
@app.route('/api/livros', methods=['GET'])
def obter_livros():
    return jsonify(app.livros)

# --- Rota POST para adicionar um novo livro ---
@app.route('/api/livros', methods=['POST'])
def adicionar_livro():
    novo_livro = request.get_json()
    max_id = max([livro['id'] for livro in app.livros], default=0)
    novo_livro['id'] = max_id + 1
    app.livros.append(novo_livro)
    return jsonify(novo_livro), 201

# --- Rota DELETE para remover um livro pelo seu ID ---
@app.route('/api/livros/<int:id>', methods=['DELETE'])
def deletar_livro(id):
    livro_existe = any(livro['id'] == id for livro in app.livros)
    if not livro_existe:
        return Response(status=404)

    app.livros = [livro for livro in app.livros if livro['id'] != id]
    return Response(status=204)

# --- Rota PUT para atualizar um livro existente ---
@app.route('/api/livros/<int:id>', methods=['PUT'])
def atualizar_livro(id):
    dados_atualizados = request.get_json()
    livro_encontrado = None

    for livro in app.livros:
        if livro['id'] == id:
            livro.update(dados_atualizados)
            livro_encontrado = livro
            break

    if livro_encontrado is None:
        return jsonify({'erro': 'Livro não encontrado'}), 404

    return jsonify(livro_encontrado), 200


if __name__ == '__main__':
    app.run(debug=True)
