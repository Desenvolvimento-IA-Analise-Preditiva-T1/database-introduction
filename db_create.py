import sqlite3

# Conecta ao banco (se o arquivo 'loja.db' não existir, o SQLite cria na hora)
conn = sqlite3.connect("loja.db")
cursor = conn.cursor()

##################################################################################
##################################################################################
# Criação das tabelas
# Clientes
cursor.execute("""
CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    cidade TEXT
);
""")

# Produtos
cursor.execute("""
CREATE TABLE IF NOT EXISTS produtos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    preco REAL NOT NULL
);
""")

# Pedidos (Relaciona o cliente e o produto via seus IDs)
cursor.execute("""
CREATE TABLE IF NOT EXISTS pedidos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cliente_id INTEGER,
    produto_id INTEGER,
    quantidade INTEGER,
    FOREIGN KEY (cliente_id) REFERENCES clientes(id),
    FOREIGN KEY (produto_id) REFERENCES produtos(id)
);
""")
##################################################################################
##################################################################################


##################################################################################
##################################################################################
# Inserção de dados simulados (INSERT)
clientes_dados = [
    ("Ana Silva", "São Paulo"),
    ("Bruno Souza", "Rio de Janeiro"),
    ("Carla Dias", "Curitiba")
]
cursor.executemany("INSERT INTO clientes (nome, cidade) VALUES (?, ?);", clientes_dados)

produtos_dados = [
    ("Teclado Mecânico", 250.00),
    ("Mouse Sem Fio", 120.00),
    ("Monitor 24pol", 890.00),
    ("Headset Gamer", 310.00)
]
cursor.executemany("INSERT INTO produtos (nome, preco) VALUES (?, ?);", produtos_dados)

pedidos_dados = [
    (1, 1, 1), # Ana comprou 1 Teclado
    (1, 2, 2), # Ana comprou 2 Mouses
    (2, 3, 1), # Bruno comprou 1 Monitor
    (3, 4, 1)  # Carla comprou 1 Headset
]
cursor.executemany("INSERT INTO pedidos (cliente_id, produto_id, quantidade) VALUES (?, ?, ?);", pedidos_dados)
##################################################################################
##################################################################################


# Salva as alterações e fecha a conexão
conn.commit()
conn.close()

print("Banco 'loja.db' criado e populado com sucesso!")
