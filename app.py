# app.py
from flask import Flask, jsonify

app = Flask(__name__)

livros = [
    { 'id': 1, 'titulo': 'O Senhor dos Anéis', 'autor': 'J.R.R. Tolkien' },
    { 'id': 2, 'titulo': 'Duna', 'autor': 'Frank Herbert' },
    { 'id': 3, 'titulo': '1984', 'autor': 'George Orwell' }
]

@app.route('/api/livros', methods=['GET'])
def obter_livros():
    return jsonify(livros)

if __name__ == '__main__':
    app.run(debug=True, port=8080)