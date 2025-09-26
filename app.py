# app.py (versão final com GET, POST, DELETE e PUT)

from flask import Flask, jsonify, request

app = Flask(__name__)

# A 'global' é necessária para que as funções possam modificar esta lista.
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

# --- Rota DELETE para remover um livro pelo seu ID ---
@app.route('/api/livros/<int:id>', methods=['DELETE'])
def deletar_livro(id):
    global livros
    
    livro_encontrado = None
    for livro in livros:
        if livro.get('id') == id:
            livro_encontrado = livro
            break
            
    if livro_encontrado is None:
        return jsonify({'erro': 'Livro não encontrado'}), 404
    
    livros = [livro for livro in livros if livro['id'] != id]
    
    return jsonify({'mensagem': 'Livro deletado com sucesso'}), 200

# --- CÓDIGO ATUALIZADO ADICIONADO ABAIXO ---

# --- Rota PUT para atualizar um livro existente pelo seu ID ---
@app.route('/api/livros/<int:id>', methods=['PUT'])
def atualizar_livro(id):
    global livros
    dados_atualizados = request.get_json()
    livro_encontrado = None
    
    # Procura o livro na lista pelo ID
    for livro in livros:
        if livro.get('id') == id:
            # Atualiza os dados do livro com o que foi enviado na requisição
            # O método .update() é perfeito para isso
            livro.update(dados_atualizados)
            livro_encontrado = livro
            break

    # Se não encontrar o livro, retorna um erro 404
    if livro_encontrado is None:
        return jsonify({'erro': 'Livro não encontrado'}), 404
    
    # Retorna o livro já com os dados atualizados
    return jsonify(livro_encontrado), 200

# --- Fim da atualização ---

if __name__ == '__main__':
    app.run(debug=True, port=8080)