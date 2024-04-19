# ---------------------------- CONEXÃO AO BANCO DE DADOS -----------------------
import oracledb
import main
# Conexão 
connection = oracledb.connect(
    user = "BD150224424",
    password = 'Qwiji4',    
    dsn = "172.16.12.14/xe")
print("Successfully Connected")
cursor = connection.cursor()

# ---------------------------- COMANDOS BANCO DE DADOS ---------------------------
# [1] MOSTRAR ESTOQUE
def mostrar_estoque():
    cursor.execute("SELECT * FROM PRODUTOS")
    estoque = cursor.fetchall() # NÃO USAR FATCHALL
    for row in estoque:
        print(row)

# [2] CRIAR TABELA  
def criar_tabela():
    cursor.execute ("""
            CREATE TABLE PRODUTOS (
                COD_PROD INTEGER NOT NULL PRIMARY KEY,
                NOME_PROD VARCHAR2(255) NOT NULL,
                DESC_PROD VARCHAR2(255) NOT NULL,
                CP NUMBER NOT NULL,
                CF NUMBER NOT NULL,
                CV NUMBER NOT NULL,
                IV NUMBER NOT NULL,
                ML NUMBER NOT NULL)""")

# [3] ADICIONAR PRODUTO
def add_produto():
    cursor.execute(f"INSERT INTO PRODUTOS VALUES ({main.codigo_produto}, {main.nome_produto}, {main.descricao_produto})")

# [4] ALTERAR COLUNA
# def add_coluna():
#     cursor.execute(f"ALTER TABLE PRODUTOS ADD COLUMN {main.nova_coluna}")

# [5] DELETAR TABELA
# def deletar_tabela():
#     cursor.execute(f"DROP TABLE PRODUTOS")

# [6] DELETAR PRODUTO
# def deletar_produto():
#     cursor.execute(f"DELETE FROM PRODUTOS WHERE NOME_PROD = '{main.nome_produto}'")

# cursor.execute ("INSERT INTO PRODUTOS VALUES (1, 'Lapis', 'Preto', 1.00, 10, 5, 18, 25)")
# cursor.execute ("INSERT INTO PRODUTOS VALUES (2, 'Lapis', 'Amarelo', 1.20, 10, 5, 18, 25)")
# cursor.execute ("INSERT INTO PRODUTOS VALUES (3, 'Lapis', 'Chines', 0.20, 10, 5, 18, 0)")