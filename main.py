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
while menu > 0:
# ---------------------------- ROTINA DE PRODUTOS -----------------------------
    if menu == 1:
        conexao.mostrar_estoque()
        print(f"""==========================================================================================================
        DESCRIÇÃO               |\t\t\tVALOR\t\t\t \t\t%

PREÇO DE VENDA                  |\t\t\tR${pv:.2f}\t\t\t \t\t100.00%
CUSTO DE AQUISIÇÃO              |\t\t\tR${valor_cp:.2f}\t\t\t \t\t{porc_aquisicao:.2f}%
RECEITA BRUTA                   |\t\t\tR${valor_rb:.2f}\t\t\t \t\t{porc_c:.2f}%
CUSTO FIXO/ADMINISTRATIVO       |\t\t\tR${valor_cf:.2f}\t\t\t \t\t{porc_cf:.2f}%
COMISSÃO DE VENDAS              |\t\t\tR${valor_cv:.2f}\t\t\t \t\t{porc_cv:.2f}%
IMPOSTOS                        |\t\t\tR${valor_iv:.2f}\t\t\t \t\t{porc_iv:.2f}%
OUTROS CUSTOS                   |\t\t\tR${outros:.2f}\t\t\t \t\t{porc_outros:.2f}%
RENTABILIDADE                   |\t\t\tR${valor_rt:.2f}\t\t\t \t\t{porc_rt:.2f}%

CLASSIFICAÇÃO DE LUCRO:        {class_lucro}
==========================================================================================================

        """)
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

        # Preço de Venda
        pv = valor_cp / (1 - ((porc_cf + porc_cv + porc_iv + porc_ml) / 100))

        # ---------------------------- CALCULOS DOS VALORES -----------------------------
        # 'porc' = porcentagem
        # 'valor' = variaveis float
        porc_aquisicao = (valor_cp * 100) / pv                            # LINHA B

        receita_bruta = pv - valor_cp                                     # LINHA C
        valor_rb = pv - valor_cp
        porc_c = 100 - porc_aquisicao

        valor_cf = (pv * porc_cf) / 100                                   # LINHA D
        valor_cv = (pv * porc_cv) / 100                                   # LINHA E
        valor_iv = (pv * porc_iv) / 100                                   # LINHA F

        outros = valor_cf + valor_cv + valor_iv                           # LINHA G
        porc_outros = porc_cf + porc_cv + porc_iv

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
        # ---------------------------- SAIDA DE VALORES -------------------------------
        os.system('cls')
        print(f'''

CÓDIGO PRODUTO: {codigo_produto}
PRODUTO: {nome_produto}
DESCRIÇÃO: {descricao_produto}

==========================================================================================================
        DESCRIÇÃO               |\t\t\tVALOR\t\t\t \t\t%

PREÇO DE VENDA                  |\t\t\tR${pv:.2f}\t\t\t \t\t100.00%
CUSTO DE AQUISIÇÃO              |\t\t\tR${valor_cp:.2f}\t\t\t \t\t{porc_aquisicao:.2f}%
RECEITA BRUTA                   |\t\t\tR${valor_rb:.2f}\t\t\t \t\t{porc_c:.2f}%
CUSTO FIXO/ADMINISTRATIVO       |\t\t\tR${valor_cf:.2f}\t\t\t \t\t{porc_cf:.2f}%
COMISSÃO DE VENDAS              |\t\t\tR${valor_cv:.2f}\t\t\t \t\t{porc_cv:.2f}%
IMPOSTOS                        |\t\t\tR${valor_iv:.2f}\t\t\t \t\t{porc_iv:.2f}%
OUTROS CUSTOS                   |\t\t\tR${outros:.2f}\t\t\t \t\t{porc_outros:.2f}%
RENTABILIDADE                   |\t\t\tR${valor_rt:.2f}\t\t\t \t\t{porc_rt:.2f}%

CLASSIFICAÇÃO DE LUCRO:        {class_lucro}
==========================================================================================================

        ''')

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

connection.commit() # Salva as informações
cursor.close() # Encerra o cursor 
connection.close()