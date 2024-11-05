from flask import Flask, request, jsonify
import sqlite3  # Ou use outro banco de dados, como PostgreSQL
from flask_cors import CORS, cross_origin  # Importando o CORS

app = Flask(__name__)
cors = CORS(app)

app.config['CORS_HEADERS'] = 'Content-Type'

# Conexão com o banco de dados
def get_db_connection():
    conn = sqlite3.connect('database.db')  # Altere para o nome do seu banco
    conn.row_factory = sqlite3.Row
    return conn

# Rota para agendar
@app.route('/api/agendar', methods=['POST'])
@cross_origin()
def agendar():
    data = request.get_json()  # Recebe dados JSON
    nome = data.get('nome')
    telefone = data.get('telefone')
    email = data.get('email')
    servico = data.get('servico')
    data_agenda = data.get('data_agenda')
    horario = data.get('horario')

    # Conexão e inserção no banco
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO agendamentos (nome, telefone, email, servico, data_agenda, horario)
                      VALUES (?, ?, ?, ?, ?, ?)''',
                   (nome, telefone, email, servico, data_agenda, horario))
    conn.commit()
    conn.close()

    return jsonify({'message': 'Agendamento criado com sucesso!'}), 201

if __name__ == '__main__':
    app.run(debug=True)
