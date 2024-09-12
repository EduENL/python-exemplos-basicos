import sqlite3

# Classe para gerenenciar a conexão com o banco de dados SQLite
class Database:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    # Cria uma tabela 'usuarios' se ela não existir 
    def create_table(self):
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            nome TEXT NOT NULL
        )
        ''')
        self.conn.commit()

    # insere um novo usuário no banco de dados
    def insert_user(self, nome):
        self.cursor.execute("INSERT INTO usuarios (nome) VALUES (?)", (nome,))
        self.conn.commit()

    # Retorna todos is usuários o banco de dados 
    def get_all_users(self):
        self.cursor.execute("SELECT * FROM usuarios")
        return self.cursor.fetchall()
    
    # Atualixa o nome de um usuário existente
    def update_user(self, id, nome):
        self.cursor.execute("DELETE FROM usuarios WHERE id=?", (id,))
        self.conn.commit()

        # Fecha a conexão com o banco de dados 
        def close(self):
            self.conn.close() 