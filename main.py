import os
from flask import Flask, request, jsonify
import sqlite3
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": ["http://127.0.0.1:5500"]}})  # Substitua pela origem específica

# Conexão com o banco de dados
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

# Rota para agendar
@app.route('/api/agendar', methods=['POST'])
def agendar():
    data = request.get_json()
    nome = data.get('nome')
    telefone = data.get('telefone')
    email = data.get('email')
    servico = data.get('servico')
    data_agenda = data.get('data_agenda')
    horario = data.get('horario')

    if not all([nome, telefone, email, servico, data_agenda, horario]):
        return jsonify({'error': 'Todos os campos são obrigatórios'}), 400

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO agendamentos (nome, telefone, email, servico, data_agenda, horario)
                      VALUES (?, ?, ?, ?, ?, ?)''', (nome, telefone, email, servico, data_agenda, horario))
    conn.commit()
    conn.close()

    return jsonify({'message': 'Agendamento criado com sucesso!'}), 201

if __name__ == '__main__':
    # Pega a porta da variável de ambiente PORT ou usa 5000 como padrão
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
