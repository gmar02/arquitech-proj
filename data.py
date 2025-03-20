import sqlite3

def carregar_dados():

    # Conectar ao banco de dados SQLite
    conn = sqlite3.connect('./instance/schema.db')
    cursor = conn.cursor()
    
    # Abrir e ler o arquivo SQL
    with open('./scripts/data.sql', 'r') as file:
        sql_script = file.read()

    # Executar o script SQL
    try:
        cursor.executescript(sql_script)
        print("Dados carregados com sucesso no schema!")
    except sqlite3.Error as e:
        print(f"Erro ao carregar dados: {e}")
    
    # Salvar as mudanças e fechar a conexão
    conn.commit()
    conn.close()