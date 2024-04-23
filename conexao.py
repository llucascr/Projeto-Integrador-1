# ---------------------------- CONEXÃO AO BANCO DE DADOS -----------------------
import oracledb
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
    for row in cursor.execute("SELECT * FROM PRODUTOS"):
        estoque = row
        print(estoque)
     # Preço de Venda
        pv = estoque[3] / (1 - ((estoque[4] + estoque[5] + estoque[6] + estoque[7]) / 100))

        # ---------------------------- CALCULOS DOS VALORES -----------------------------
        # 'porc' = porcentagem
        # 'valor' = variaveis float
        porc_aquisicao = (estoque[3] * 100) / pv                            # LINHA B

        receita_bruta = pv - estoque[3]                                     # LINHA C
        valor_rb = pv - estoque[3]
        porc_c = 100 - porc_aquisicao

        valor_cf = (pv * estoque[4]) / 100       #cf                            # LINHA D
        valor_cv = (pv * estoque[5]) / 100       #cv                            # LINHA E
        valor_iv = (pv * estoque[6]) / 100       #iv                            # LINHA F

        outros = valor_cf + valor_cv + valor_iv                           # LINHA G
        porc_outros = estoque[4] + estoque[5] + estoque[6]
        
        valor_rt = valor_rb - outros                                      # LINHA H
        # Porcentual de Rentabilidade
        porc_rt = porc_c - porc_outros
        # ---------------------------- CLASSIFICAÇÃO DE LUCRO -----------------------------
        if porc_rt > 20:
            class_lucro = "Alto"
        elif 10 <= porc_rt <= 20:
            class_lucro = "Médio"
        elif 0 < porc_rt < 10:
            class_lucro = "Baixo"
        elif porc_rt == 0:
            class_lucro = "Equilibrio"
        else:
            class_lucro = "Prejuizo"

        print(f'''

CÓDIGO PRODUTO: {estoque[0]}
PRODUTO: {estoque[1]}
DESCRIÇÃO: {estoque[2]}

==========================================================================================================
        DESCRIÇÃO               |\t\t\tVALOR\t\t\t \t\t%

PREÇO DE VENDA                  |\t\t\tR${pv:.2f}\t\t\t \t\t100.00%
CUSTO DE AQUISIÇÃO              |\t\t\tR${estoque[3]:.2f}\t\t\t \t\t{porc_aquisicao:.2f}%
RECEITA BRUTA                   |\t\t\tR${valor_rb:.2f}\t\t\t \t\t{porc_c:.2f}%
CUSTO FIXO/ADMINISTRATIVO       |\t\t\tR${valor_cf:.2f}\t\t\t \t\t{estoque[4]:.2f}%
COMISSÃO DE VENDAS              |\t\t\tR${valor_cv:.2f}\t\t\t \t\t{estoque[5]:.2f}%
IMPOSTOS                        |\t\t\tR${valor_iv:.2f}\t\t\t \t\t{estoque[6]:.2f}%
OUTROS CUSTOS                   |\t\t\tR${outros:.2f}\t\t\t \t\t{porc_outros:.2f}%
RENTABILIDADE                   |\t\t\tR${valor_rt:.2f}\t\t\t \t\t{porc_rt:.2f}%

CLASSIFICAÇÃO DE LUCRO:        {class_lucro}
==========================================================================================================

        ''')


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
    cursor.execute(f"INSERT INTO PRODUTOS VALUES ()")

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