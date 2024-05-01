#------------------------------------------------------------------------------------------------#
                         #CONEXÃO COM O BANCO DE DADOS,CURSOR E LIMPEZA
import os
import oracledb
connection = oracledb.connect(user = "BD150224212", password = "Dsiow3", dsn = "172.16.12.14/xe")
cursor = connection.cursor()
#------------------------------------------------------------------------------------------------#
                                          #FUNÇÕES
def CALCULO_TABELA(): #CALCULA OS VALORES DA TABELA E IMPRIME

    PV = CP/(1-((CF+CV+IV+ML)/100)) #CALCULAR O VALOR PARA VENDA DO PRODUTO

    OCpor = CF+CV+IV          #OUTROS CUSTOS '%'
    CFnum = (PV*CF)/100       #CUSTO FIXO 'VALOR'
    CVnum = (PV*CV)/100       #COMISSAO 'VALOR'
    IVnum = (PV*IV)/100       #IMPOSTOS 'VALOR'
    OCnum = CFnum+CVnum+IVnum #OUTROS CUSTOS 'VALOR'
    RBnum = PV-CP             #RECEITA BRUTA 'VALOR'
    Rnum  = RBnum-OCnum       #RENTABILIDADE 'VALOR'
    CPpor = (CP*100)/PV       #CUSTO PRODUTO '%'
    RBpor = 100-CPpor         #RECEITA BRUTA '%'
    Rpor  = RBpor-OCpor       #RENTABILIDADE '%'

    if Rpor > 20:
        ClassLucro = 'LUCRO ALTO'
    elif 10 <= Rpor <= 20:
        ClassLucro = 'LUCRO MÉDIO'
    elif 0 < Rpor < 10:
        ClassLucro = 'LUCRO BAIXO'
    elif Rpor == 0:
        ClassLucro = 'EQUILÍBRIO'
    elif Rpor < 0:
        ClassLucro = 'PREJUÍZO'

    print(f'''
                 

=================================================================
¦ CÓDIGO: {cod_prod}\t\t\t\t\t\t
¦ PRODUTO: {nome_prod}\t\t\tVALOR\t¦\t%\t
¦ DESCRIÇÃO: {desc_prod}\t\t\t\t\t\t           
=================================================================
¦ A. Preço de Venda\t\t¦ R${PV:.2f}\t¦  100.00%\t¦
¦ B. Custo de Aquisição\t\t¦ R${CP:.2f}\t¦  {CPpor:.2f}%\t¦    
¦ C. Receita Bruta(A-B)\t\t¦ R${RBnum:.2f}\t¦  {RBpor:.2f}%\t¦  
¦ D. Custo Fixo/Administrativo\t¦ R${CFnum:.2f}\t¦  {CF:.2f}%\t¦                     
¦ E. Comissão de Vendas\t\t¦ R${CVnum:.2f}\t¦  {CV:.2f}%\t¦
¦ F. Impostos\t\t\t¦ R${IVnum:.2f}\t¦  {IV:.2f}%\t¦
¦ G. Outros Custos(D+E+F)\t¦ R${OCnum:.2f}\t¦  {OCpor:.2f}%\t¦
¦ H. Rentabilidade(C-G)\t\t¦ R${Rnum:.2f}\t¦  {Rpor:.2f}%\t¦
=================================================================
¦ CLASSIFICAÇÃO DE LUCRO:\t {ClassLucro}\t\t\t¦
=================================================================



        ''')
    connection.commit()

#------------------------------------------------------------------------------------------------#
                                #MENU PARA ENTRAR NO LOOP
os.system('cls')
MENU = int(input("""
=================================================================
¦                          BEM VINDO AO                         ¦
¦                  SISTEMA DE CADASTRO DE PRODUTO!!!            ¦
=================================================================
¦ OPÇÕES:                                                       ¦
=================================================================
¦ [1].CADASTRAR PRODUTO                                         ¦
¦ [2].ALTERAR PRODUTO                                           ¦
¦ [3].APAGAR PRODUTO/ESTOQUE                                    ¦
¦ [4].MOSTRAR PRODUTO/ESTOQUE                                   ¦
¦ [0].SAIR                                                      ¦                                                     
=================================================================
                    OPÇÃO: """))

os.system('cls')
#------------------------------------------------------------------------------------------------#
                 #LOOP PARA CADASTRO, ALTERAÇÃO, EXCLUSÃO E PRINT DO PRODUTO OU ESTOQUE
while (MENU != 0):   
                                         
    if  (MENU==1): #CADASTRAR PRODUTO
        cod_prod = int(input('Código do Produto: '))         #CODIGO DO PRODUTO
        nome_prod = str(input('Nome Produto: '))             #NOME DO PRODUTO
        desc_prod = str(input('Descrição do Produto: '))     #DESCRIÇÃO DO PRODUTO

        CP = float(input('Custo do  Produto: '))             #CUSTO PAGO PELO PRODUTO PARA O FORNECEDOR
        ML = float(input('Margem de Lucro sobre a Venda: ')) #MARGEM DE LUCRO SOBRE A VENDA DO PRODUTO
        CF = float(input('Custo Fixo/Administrativo(%): '))  #CUSTO FIXO (ESPAÇO FÍSICO, DESPESAS, FUNCIONÁRIOS...)
        CV = float(input('Comissão de Vendas(%): '))         #COMISSÃO SOBRE A VENDA DO PRODUTO
        IV = float(input('Impostos(%): '))                   #IMPOSTOS SOBRE A VENDA DO PRODUTO
 
        cursor.execute("INSERT INTO estoque VALUES (:1, :2, :3, :4, :5, :6, :7, :8)",(cod_prod, nome_prod, desc_prod, CP, CF, CV, IV, ML))
        connection.commit()

        os.system('cls')     
        
        CALCULO_TABELA()

        print('''
                  PRODUTO CADASTRADO COM SUCESSO!!!''')
    elif(MENU==2): #ALTERAR PRODUTO
        print("AINDA TRABALHANDO NISSO :(")
    elif(MENU==3): #APAGAR PRODUTO/ESTOQUE
        opcao_apagar=int(input("APAGAR [1]ESTOQUE OU [2]PRODUTO: "))

        if(opcao_apagar==1):
            cursor.execute("DELETE FROM estoque")
            connection.commit()
            print('''
                  ESTOQUE APAGADO COM SUCESSO!!!''')
            
        elif(opcao_apagar==2):
            cod_apagar=int(input("Digite o codigo do produto que deseja apagar: "))
          
            cursor.execute("DELETE FROM estoque WHERE cod_prodT = :1",(cod_apagar,))
            connection.commit()
            print('''
                  PRODUTO APAGADO COM SUCESSO!!!''')
    elif(MENU==4): #MOSTRAR PRODUTO/ESTOQUE
        opcao_mostrar=int(input("MOSTRAR [1]ESTOQUE OU [2]PRODUTO: "))

        if(opcao_mostrar==1):
            cursor.execute("SELECT * FROM estoque")
            for row in cursor:

                cod_prod  = row[0]
                nome_prod = row[1]
                desc_prod = row[2]
                CP = row[3]
                CF = row[4]
                CV = row[5]
                IV = row[6]
                ML = row[7]  

                CALCULO_TABELA()

        elif(opcao_mostrar==2):
            cod_mostrar=int(input("Digite o codigo do produto que deseja mostrar: "))
          
            cursor.execute("SELECT * FROM estoque WHERE cod_prodT = :1", (cod_mostrar,))
            for row in cursor:

                cod_prod  = row[0]
                nome_prod = row[1]
                desc_prod = row[2]
                CP = row[3]
                CF = row[4]
                CV = row[5]
                IV = row[6]
                ML = row[7]

                CALCULO_TABELA()

    MENU= int(input("""
                
-----------------------------------------------------------------
                                       
=================================================================
¦ OPÇÕES:                                                       ¦
=================================================================                    
¦ [1].CADASTRAR PRODUTO                                         ¦
¦ [2].ALTERAR PRODUTO                                           ¦
¦ [3].EXCLUIR PRODUTO/ESTOQUE                                   ¦
¦ [4].MOSTRAR PRODUTO/ESTOQUE                                   ¦
¦ [0].SAIR                                                      ¦
=================================================================
                    OPÇÃO: """))
    
    os.system('cls')
#------------------------------------------------------------------------------------------------#
                     #DESPEDIDA, ULTIMO COMMIT, TERMINAR CONEXAO E O CURSOR
print("TCHAU BRIGADO :) ")

connection.commit()
cursor.close()
connection.close()
#------------------------------------------------------------------------------------------------#

