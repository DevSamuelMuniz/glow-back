import sqlite3

# Função para criar o banco de dados e a tabela
def create_database():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Criação da tabela 'schedule'
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS agendamentos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            telefone TEXT NOT NULL,
            email TEXT NOT NULL,
            servico TEXT NOT NULL,
            data_agenda TEXT NOT NULL,
            horario TEXT NOT NULL
        )
    ''')

    conn.commit()
    conn.close()
    print("Banco de dados e tabela criados com sucesso.")

# Executa a função
if __name__ == '__main__':
    create_database()
