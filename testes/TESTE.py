import os
import oracledb
connection = oracledb.connect(user = "BD150224212", password = "Dsiow3", dsn = "172.16.12.14/xe")
cursor = connection.cursor()

#DROPAR A TABELA CASO JA EXISTA
cursor.execute("DROP TABLE estoque")

#CRIAR A TABELA CASO AINDA NAO EXISTA
cursor.execute("""
    CREATE TABLE estoque(
    cod_prodT INT PRIMARY KEY,
    nome_prodT VARCHAR2(100),
    desc_prodT VARCHAR2(100),
    cpT NUMBER(10,2),
    cfT NUMBER(10,2),
    cvT NUMBER(10,2),
    ivT NUMBER(10,2),
    mlT NUMBER(10,2)        
    )
""")


MENU = int(input("""
=================================================================
                          BEM VINDO AO
                  SISTEMA DE CADASTRO DE PRODUTO!!!
=================================================================
OPÇÕES:
[1].CADASTRAR PRODUTO
[2].ALTERAR PRODUTO
[3].EXCLUIR PRODUTO/ESTOQUE
[4].MOSTRAR PRODUTO/ESTOQUE
[0].SAIR
=================================================================
                    OPÇÃO: """))
os.system('cls')

while (MENU != 0):   
                                         
    if  (MENU==1): #CADASTRAR PRODUTO
        cod_prod = int(input('Código do Produto: '))       #CODIGO DO PRODUTO
        nome_prod = str(input('Nome Produto: '))              #NOME DO PRODUTO
        desc_prod = str(input('Descrição do Produto: ')) #DESCRIÇÃO DO PRODUTO

        CP = float(input('Custo do  Produto: '))              #CUSTO PAGO PELO PRODUTO PARA O FORNECEDOR
        ML = float(input('Margem de Lucro sobre a Venda: '))  #MARGEM DE LUCRO SOBRE A VENDA DO PRODUTO
        CF = float(input('Custo Fixo/Administrativo(%): '))    #CUSTO FIXO (ESPAÇO FÍSICO, DESPESAS, FUNCIONÁRIOS...)
        CV = float(input('Comissão de Vendas(%): '))          #COMISSÃO SOBRE A VENDA DO PRODUTO
        IV = float(input('Impostos(%): '))                    #IMPOSTOS SOBRE A VENDA DO PRODUTO
#------------------------------------------------------------------------------------------------------------------------#
                                             #VERIFICAÇÃO DE VALORES VALIDOS NO CADASTRO
        if (CP < 0):
            print("VALOR INVÁLIDO!!! PARA 'CUSTO DO PRODUTO'. ")
            CP = float(input('Custo do  Produto: '))             
        if (ML < 0):
            print("VALOR INVÁLIDO!!! PARA 'MARGEM DE LUCRO'. ")
            ML = float(input('Margem de Lucro sobre a Venda: '))  
        if (CF < 0):
            print("VALOR INVÁLIDO!!! PARA 'CUSTO FIXO'. ")
            CF = float(input('Custo Fixo/Administrativo(%): '))    
        if (CV < 0):
            print("VALOR INVÁLIDO!!! PARA 'COMISSAO DE VENDAS'. ")
            CV = float(input('Comissão de Vendas(%): '))         
        if (IV < 0):
            print("VALOR INVÁLIDO!!! PARA 'IMPOSTOS'. ")
            IV = float(input('Impostos(%): '))  
#------------------------------------------------------------------------------------------------------------------------#
                        #COMANDO PARA INSERIR OS DADOS NA TABELA     
        cursor.execute("INSERT INTO estoque (cod_prodT, nome_prodT, desc_prodT, cpT, cfT, cvT, ivT, mlT) VALUES (:1, :2, :3, :4, :5, :6, :7, :8)",(cod_prod, nome_prod, desc_prod, CP, CF, CV, IV, ML))
        connection.commit()

        os.system('cls')     
#------------------------------------------------------------------------------------------------------------------------#
                                              #CALCULOS DO PRODUTO

        PV = CP/(1-((CF+CV+IV+ML)/100)) #CALCULAR O VALOR PARA VENDA DO PRODUTO

        OC    = CF+CV+IV      #OUTROS CUSTOS '%'
        CFnum = (PV*CF)/100   #CUSTO FIXO 'VALOR'
        CVnum = (PV*CV)/100   #COMISSAO 'VALOR'
        IVnum = (PV*IV)/100   #IMPOSTOS 'VALOR'
        OCnum = (PV*OC)/100   #OUTROS CUSTOS 'VALOR'
        RB    = PV-CP         #RECEITA BRUTA 'VALOR'
        Rnum  = RB-OCnum      #RENTABILIDADE 'VALOR'
        Rpor  = (Rnum*100)/PV #RENTABILIDADE '%'
        CPpor = (CP*100)/PV   #CUSTO PRODUTO '%'
        RBpor = 100-CPpor     #RECEITA BRUTA '%'
#------------------------------------------------------------------------------------------------------------------------#
                                            #VERIFICAÇÃO DA CLASSIFICACAO DE LUCRO
        if Rpor > 20:
            ClassLucro = 'LUCRO ALTO'
        elif 10 <= Rpor <= 20:
            ClassLucro = 'LUCRO MÉDIO'
        elif 0 <= Rpor <= 10:
            ClassLucro = 'LUCRO BAIXO'
        elif Rpor == 0:
            ClassLucro = 'EQUILÍBRIO'
        elif Rpor < 0:
            ClassLucro = 'PREJUÍZO'
#------------------------------------------------------------------------------------------------------------------------#
                                        #IMPRIMINDO TABELA COM O CALCULO DO PRODUTO            
        print(f'''
                 CADASTRADO COM SUCESSO!!!
=================================================================
¦ CÓDIGO PRODUTO: {cod_prod}\t\t¦\t\t¦\t\t¦
¦ PRODUTO: {nome_prod}\t\t¦\tVALOR\t¦\t%\t¦
¦ DESCRIÇÃO: {desc_prod}\t\t¦\t\t¦\t\t¦           
=================================================================
¦ A. Preço de Venda             ¦\tR%{PV:.2f}\t¦\t100.00%\t¦
¦ B. Custo de Aquisição         ¦\tR%{CP:.2f}\t¦\t{CPpor:.2f}%\t¦    
¦ C. Receita Bruta(A-B)         ¦\tR%{RB:.2f}\t¦\t{RBpor:.2f}%\t¦  
¦ D. Custo Fixo/Administrativo  ¦\tR%{CFnum:.2f}\t¦\t{CF:.2f}%\t¦                     
¦ E. Comissão de Vendas         ¦\tR%{CVnum:.2f}\t¦\t{CV:.2f}%\t¦
¦ F. Impostos                   ¦\tR%{IVnum:.2f}\t¦\t{IV:.2f}%\t¦
¦ G. Outros Custos(D+E+F)       ¦\tR%{OCnum:.2f}\t¦\t{OC:.2f}%\t¦
¦ H. Rentabilidade(C-G)         ¦\tR%{Rnum:.2f}\t¦\t{Rpor:.2f}%\t¦
=================================================================
¦CLASSIFICAÇÃO DE LUCRO:        ¦\t{ClassLucro}\t\t¦
=================================================================

        ''')
    elif(MENU==2): #ALTERAR PRODUTO
        print("AINDA TRABALHANDO NISSO :(")
    elif(MENU==3): #EXCLUIR PRODUTO/ESTOQUE
        ex_prod_est=int(input("APAGAR [1]ESTOQUE OU [2]PRODUTO: "))

        if(ex_prod_est==1):
            cursor.execute("DELETE FROM estoque")
            print("ESTOQUE APAGADO COM SUCESSO!!!")

        elif(ex_prod_est==2):
            info_cod_e=int(input("Digite o codigo do produto que deseja apagar: "))
            cursor.execute("DELETE FROM estoque WHERE cod_prodT = :1",(info_cod_e,))
            print("PRODUTO APAGADO COM SUCESSO!!!")
    elif(MENU==4): #MOSTRAR PRODUTO/ESTOQUE
        mos_prod_est=int(input("MOSTRAR [1]ESTOQUE OU [2]PRODUTO: "))

        if(mos_prod_est==1):
            cursor.execute("SELECT * FROM estoque")
            for row in cursor:
                print(row)

        elif(mos_prod_est==2):
            info_cod_m=int(input("Digite o codigo do produto que deseja mostrar: "))
            cursor.execute("SELECT * FROM estoque WHERE cod_prodT = :1", (info_cod_m,))
            for row in cursor:
                print(row)

    MENU= int(input("""
                    
=================================================================
OPÇÕES:
[1].CADASTRAR PRODUTO
[2].ALTERAR PRODUTO
[3].EXCLUIR PRODUTO/ESTOQUE
[4].MOSTRAR PRODUTO/ESTOQUE
[0].SAIR
=================================================================
                    OPÇÃO: """))
    os.system('cls')
print("TCHAU BRIGADO :) ")
