from flask import Flask, request, jsonify
from pymongo import MongoClient
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": ["https://senacglowtime.netlify.app"]}})  # Substitua pela origem específica

# Conexão com o MongoDB Atlas
client = MongoClient('mongodb+srv://recinproj:NRdhqU14UA14vJF5@cluster0.r8fkm.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
db = client['glowRec']  # Substitua com o nome do banco de dados
agendamentos_collection = db.agendamentos  # Nome da coleção

# Rota para agendar
@app.route('/api/agendar', methods=['POST'])
@cross_origin()
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

    # Insere o agendamento no MongoDB
    agendamento = {
        'nome': nome,
        'telefone': telefone,
        'email': email,
        'servico': servico,
        'data_agenda': data_agenda,
        'horario': horario
    }
    agendamentos_collection.insert_one(agendamento)

    return jsonify({'message': 'Agendamento criado com sucesso!'}), 201


# @app.router('/api/gerenciamento', methods=['GET'])
# @cross_origin()
# def receberGerenciamento():
    

if __name__ == '__main__':
    # Pega a porta da variável de ambiente PORT ou usa 5000 como padrão
    port = 5000
    app.run(host='0.0.0.0', port=port, debug=True)
