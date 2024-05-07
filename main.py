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
=================================================================
                          BEM VINDO AO
                  SISTEMA DE CADASTRO DE PRODUTO!!!
=================================================================
OPÇÕES:
[1].CADASTRAR PRODUTOS
[2].ALTERAR PRODUTOS
[3].APAGAR PRODUTOS
[4].LISTAR PRODUTOS
[5].SAIR
[0].CRIAR TABELA
[-1].DELETAR TABELA 
=================================================================
                    OPÇÃO: """))
os.system('cls')

while menu != 5:
# ---------------------------- ROTINA DE PRODUTOS -----------------------------
    if menu == 1: #CADASTRAR PRODUTOS
# ---------------------------- CADASTRO DOS PRODUTOS ----------------------------
        cod_prod = int(input('Código do Produto: '))       #CODIGO DO PRODUTO
        nome_prod = str(input('Nome Produto: '))           #NOME DO PRODUTO
        desc_prod = str(input('Descrição do Produto: '))   #DESCRIÇÃO DO PRODUTO

        CP = float(input('Custo do  Produto: '))              #CUSTO PAGO PELO PRODUTO PARA O FORNECEDOR
        ML = float(input('Margem de Lucro sobre a Venda: '))  #MARGEM DE LUCRO SOBRE A VENDA DO PRODUTO
        CF = float(input('Custo Fixo/Administrativo(%): '))   #CUSTO FIXO (ESPAÇO FÍSICO, DESPESAS, FUNCIONÁRIOS...)
        CV = float(input('Comissão de Vendas(%): '))          #COMISSÃO SOBRE A VENDA DO PRODUTO
        IV = float(input('Impostos(%): '))                    #IMPOSTOS SOBRE A VENDA DO PRODUTO

        os.system('cls')

        cursor.execute(f"INSERT INTO produtos VALUES ({cod_prod}, '{nome_prod}', '{desc_prod}', {CP}, {CF},{CV}, {IV}, {ML})")
        connection.commit()
        
        conexao.mostrar_estoque()

        print("""
                    PRODUTO CADASTRADO COM SUCESSO!!!
              """)
    # elif menu == 2: #ALTERAR PRODUTOS
        # jhe coloca o codigo seu aqui
    elif menu == 3: #CADASTRAR PRODUTO
        conexao.deletar_produto()
    elif menu == 4: #LISTAR PRODUTOS
        print("""
                        ESTOQUE COMPLETO!!!""")
        conexao.mostrar_estoque()
        # conexao.deletar_tabela()
    elif menu == 0: #CRIAR TABELA
        conexao.criar_tabela()
        print("""
                    TABELA CRIADA COM SUCESSO!!!""")
    elif menu == -1:
        conexao.deletar_tabela()
    
    menu = int(input("""
=================================================================
                          BEM VINDO AO
                  SISTEMA DE CADASTRO DE PRODUTO!!!
=================================================================
OPÇÕES:
[1].CADASTRAR PRODUTOS
[2].ALTERAR PRODUTOS
[3].APAGAR PRODUTOS
[4].LISTAR PRODUTOS
[5].SAIR
[0].CRIAR TABELA
[-1].DELETAR TABELA 
=================================================================
                    OPÇÃO: """))
    
    os.system('cls')
    # ---------------------------- FIM ROTINA DE PRODUTOS -----------------------------
connection.commit()
cursor.close()
connection.close()
