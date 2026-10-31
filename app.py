import sqlite3

# Conecta a um banco de dados em memória para testes
conn = sqlite3.connect(':memory:')
cursor = conn.cursor()

# Criação de tabela e inserção de dados de teste
cursor.execute("CREATE TABLE usuarios (id INTEGER PRIMARY KEY, usuario TEXT, senha TEXT)")
cursor.execute("INSERT INTO usuarios (usuario, senha) VALUES ('admin', 'SenhaSuperSecreta123')")
cursor.execute("INSERT INTO usuarios (usuario, senha) VALUES ('user1', 'MinhaSenha456')")
conn.commit()

print("--- TELA DE LOGIN (VULNERÁVEL) ---")
username_input = input("Usuário: ")
password_input = input("Senha: ")

# VULNERABILIDADE: Concatenação direta da entrada do usuário na query SQL
query = f"SELECT * FROM usuarios WHERE usuario = '{username_input}' AND senha = '{password_input}'"

print(f"\n[DEBUG] Consulta executada no banco:\n{query}\n")

try:
    cursor.execute(query)
    resultado = cursor.fetchall()

    if resultado:
        print(f"Login bem-sucedido! Dados do usuário: {resultado}")
    else:
        print("Falha no login: Usuário ou senha incorretos.")
except sqlite3.OperationalError as e:
    print(f"Erro de sintaxe SQL: {e}")