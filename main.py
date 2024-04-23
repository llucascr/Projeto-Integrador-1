import os
import oracledb
import conexao
connection = oracledb.connect(
    user = "BD150224424",
    password = 'Qwiji4',    
    dsn = "172.16.12.14/xe")
print("Successfully Connected")
cursor = connection.cursor()
os.system('cls')
# ---------------------------- MENU DE COMANDOS ------------------------------
menu = int(input("""
        [1] MOSTRAR ESTOQUE
        [2] CRIAR TABELA   
        [3] ADICIONAR PRODUTO
        [4] ALTERAR COLUNA
        [5] DELETAR TABELA
        [6] DELETAR PRODUTO
        [0] SAIR DO PROGRAMA
        """))
while menu != 0:
# ---------------------------- ROTINA DE PRODUTOS -----------------------------
    if menu == 1:
        conexao.mostrar_estoque()
    elif menu == 2:
        conexao.criar_tabela()
        print("Tabela Criada com Sucesso")
    elif menu == 3:
        # ---------------------------- CADASTRO DOS PRODUTOS ----------------------------
        print("="*47)
        print("\tSISTEMA DE CADASTRO DE PRODUTOS")
        print("="*47)

        print(">>> Insira os dados do produto:")

        codigo_produto = int(input("Código do Prouduto: "))
        nome_produto = str(input("Nome do Produto: "))
        descricao_produto = str(input("Descrição do Produto: "))

        os.system('cls')
        # ---------------------------- CADASTRO DOS PRODUTOS ----------------------------
        print("="*47)
        print("\tSISTEMA DE CADASTRO DE PRODUTOS")
        print("="*47)

        print(">>> Insira os dados do produto:")

        valor_cp = float(input("Custo do Produto (CP): "))
        porc_cf = float(input("Custo Fixo do Produto (CF): "))
        porc_cv = float(input("Comissão de Vendas (CV): "))
        porc_iv = float(input("Impostos (IV): "))
        porc_ml = float(input("Rentabilidade (ML): "))
        os.system('cls')
        # conexao.add_produto()
    elif menu == 4:
        nova_coluna = str(input("Nome e tipo da coluna: ")).upper
        conexao.add_coluna()
    elif menu == 5:
        conexao.deletar_tabela()
    elif menu == 6:
        conexao.deletar_produto()
    
    menu = int(input("""
        [1] MOSTRAR ESTOQUE
        [2] CRIAR TABELA   
        [3] ADICIONAR PRODUTO
        [4] ALTERAR COLUNA
        [5] DELETAR TABELA
        [6] DELETAR PRODUTO
        [0] SAIR DO PROGRAMA
        """))

cursor.close() # Encerra o cursor 
connection.close()