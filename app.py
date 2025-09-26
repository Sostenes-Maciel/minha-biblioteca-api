# app.py (versão final com GET, POST e DELETE)

from flask import Flask, jsonify, request

app = Flask(__name__)

# A 'global' é necessária para que a função 'deletar_livro' possa modificar esta lista.
global livros
livros = [
    { 'id': 1, 'titulo': 'O Senhor dos Anéis', 'autor': 'J.R.R. Tolkien' },
    { 'id': 2, 'titulo': 'Duna', 'autor': 'Frank Herbert' },
    { 'id': 3, 'titulo': '1984', 'autor': 'George Orwell' }
]

# --- Rota GET para obter todos os livros ---
@app.route('/api/livros', methods=['GET'])
def obter_livros():
    return jsonify(livros)

# --- Rota POST para adicionar um novo livro ---
@app.route('/api/livros', methods=['POST'])
def adicionar_livro():
    novo_livro = request.get_json()
    novo_livro['id'] = len(livros) + 1
    livros.append(novo_livro)
    return jsonify(novo_livro), 201

# --- MODIFICAÇÃO NECESSÁRIA ADICIONADA ABAIXO ---

# --- Rota DELETE para remover um livro pelo seu ID ---
@app.route('/api/livros/<int:id>', methods=['DELETE'])
def deletar_livro(id):
    global livros # Avisa que vamos modificar a variável 'livros' global
    
    # Verifica se um livro com o ID fornecido existe
    livro_encontrado = None
    for livro in livros:
        if livro.get('id') == id:
            livro_encontrado = livro
            break
            
    # Se não encontrar o livro, retorna um erro 404
    if livro_encontrado is None:
        return jsonify({'erro': 'Livro não encontrado'}), 404
    
    # Recria a lista de livros, excluindo o livro com o ID correspondente
    livros = [livro for livro in livros if livro['id'] != id]
    
    # Retorna uma mensagem de sucesso
    return jsonify({'mensagem': 'Livro deletado com sucesso'}), 200

# --- Fim da modificação ---

if __name__ == '__main__':
    app.run(debug=True, port=8080)