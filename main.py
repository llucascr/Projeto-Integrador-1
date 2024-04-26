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
[1].MOSTRAR PRODUTO/ESTOQUE
[2].CRIAR TABELA
[3].CADASTRAR PRODUTO
[4].DELETAR TABELA
[5].DELETAR PRODUTOS
[0].SAIR
=================================================================
                    OPÇÃO: """))
os.system('cls')

while menu != 0:
# ---------------------------- ROTINA DE PRODUTOS -----------------------------
    if menu == 1: #MOSTRAR ESTOQUE
        print("""
                        ESTOQUE COMPLETO!!!""")
        conexao.mostrar_estoque()
    elif menu == 2: #CRIAR TABELA
        conexao.criar_tabela()
        print("""
                    TABELA CRIADA COM SUCESSO!!!""")
    elif menu == 3: #CADASTRAR PRODUTO
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

        cursor.execute("INSERT INTO produtos VALUES (:1, :2, :3, :4, :5, :6, :7, :8)",(cod_prod, nome_prod, desc_prod, CP, CF, CV, IV, ML))
        connection.commit()
        
        conexao.mostrar_estoque()

        print("""
                    PRODUTO CADASTRADO COM SUCESSO!!!
              """)
    elif menu == 4: #APAGAR TABELA
        conexao.deletar_tabela()
    elif menu == 5: #DELETAR TODOS PRODUTOS
        conexao.deletar_produto()
    
    menu = int(input("""

=================================================================
OPÇÕES:
[1].MOSTRAR PRODUTO/ESTOQUE
[2].CRIAR TABELA
[3].CADASTRAR PRODUTO
[4].DELETAR TABELA
[5].DELETAR PRODUTOS
[0].SAIR
=================================================================
                    OPÇÃO: """))
    
    os.system('cls')
    # ---------------------------- FIM ROTINA DE PRODUTOS -----------------------------
connection.commit()
cursor.close()
connection.close()
