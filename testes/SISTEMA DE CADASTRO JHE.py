#------------------------------------------------------------------------------------------------#
                         #CONEXÃO COM O BANCO DE DADOS,CURSOR E LIMPEZA
import os
import oracledb
connection = oracledb.connect(user = "XXXXX", password = "XXXXXX", dsn = "172.16.12.14/xe")
cursor = connection.cursor()

os.system('cls')
#------------------------------------------------------------------------------------------------#
                                          #FUNÇÕES
def CALCULO_TABELA():  #CALCULA OS VALORES DA TABELA E IMPRIME

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
=========================================================
¦ CÓDIGO: {cod_prod}\t\t\t\t\t\t
¦ PRODUTO: {nome_prod}\t\t\tVALOR\t  %
¦ DESCRIÇÃO: {desc_prod}\t\t\t\t\t\t           
=========================================================
¦ A. Preço de Venda\t\t¦ R${PV:.2f}\t¦  100%\t¦
¦ B. Custo de Aquisição\t\t¦ R${CP:.2f}\t¦  {CPpor:.0f}% \t¦   
¦ C. Receita Bruta(A-B)\t\t¦ R${RBnum:.2f}\t¦  {RBpor:.0f}% \t¦  
¦ D. Custo Fixo/Administrativo\t¦ R${CFnum:.2f}\t¦  {CF:.0f}% \t¦                     
¦ E. Comissão de Vendas\t\t¦ R${CVnum:.2f}\t¦  {CV:.0f}% \t¦
¦ F. Impostos\t\t\t¦ R${IVnum:.2f}\t¦  {IV:.0f}% \t¦
¦ G. Outros Custos(D+E+F)\t¦ R${OCnum:.2f}\t¦  {OCpor:.0f}% \t¦
¦ H. Rentabilidade(C-G)\t\t¦ R${Rnum:.2f}\t¦  {Rpor:.0f}% \t¦
=========================================================
¦ CLASSIFICAÇÃO DE LUCRO:\t {ClassLucro}\t\t¦
=========================================================
        ''')
    connection.commit()
def ALTERAR_PRODUTO(): #ALTERAR PRODUTO
    cod_alterar = int(input('Digite o codigo do produto que deseja alterar: '))
    menu_alterar = int(input('''                   
=============================
¦ O QUE DESEJA ALTERAR:     ¦
=============================
¦ [1].NOME                  ¦
¦ [2].DESCRICAO             ¦
¦ [3].CUSTO DO PRODUTO      ¦
¦ [4].MARGEM DE LUCRO       ¦
¦ [5].CUSTO FIXO            ¦
¦ [6].COMISSAO DE VENDAS    ¦
¦ [7].IMPOSTOS              ¦                                                     
=============================
        OPÇÃO: '''))   
        
    if (menu_alterar == 1):
        alteracao = str(input('NOVO Nome Produto: '))
        cursor.execute(f"UPDATE produtos SET nome_prod = '{alteracao}' WHERE cod_prod = {cod_alterar}")
            
    elif (menu_alterar == 2):
        alteracao = str(input('NOVA Descrição do Produto: '))
        cursor.execute(f"UPDATE produtos SET desc_prod = '{alteracao}' WHERE cod_prod = {cod_alterar}")         

    elif (menu_alterar == 3):
        alteracao = float(input('NOVO Custo do  Produto: '))
        cursor.execute(f"UPDATE produtos SET cp = {alteracao} WHERE cod_prod = {cod_alterar}")
            
    elif (menu_alterar == 4):
        alteracao = float(input('NOVA Margem de Lucro sobre a Venda: '))
        cursor.execute(f"UPDATE produtos SET ml = {alteracao} WHERE cod_prod = {cod_alterar}")
            
    elif (menu_alterar == 5):
        alteracao = float(input('NOVO Custo Fixo/Administrativo(%): '))
        cursor.execute(f"UPDATE produtos SET cf = {alteracao} WHERE cod_prod = {cod_alterar}")

    elif (menu_alterar == 6):
        alteracao = float(input('NOVA Comissão de Vendas(%): '))
        cursor.execute(f"UPDATE produtos SET cv = {alteracao} WHERE cod_prod = {cod_alterar}")

    elif (menu_alterar == 7):
        alteracao = float(input('NOVO Impostos(%)?: '))
        cursor.execute(f"UPDATE produtos SET iv = {alteracao} WHERE cod_prod = {cod_alterar}")
    
    connection.commit()

    print('''
        PRODUTO ALTERADO COM SUCESSO!!!''')
def APAGAR_PRODUTO():  #APAGAR PRODUTO
    cod_apagar = int(input('Digite o codigo do produto que deseja apagar: '))
    sim_nao = str(input('CONFIRMAR A EXCLUSÃO DO PRODUTO <S/N>: ')).upper()

    while (sim_nao == 'N'):
        cod_apagar = int(input('Digite o codigo do produto que deseja apagar: '))
        sim_nao = str(input('CONFIRMAR A EXCLUSÃO DO PRODUTO <S/N>: ')).upper()

    cursor.execute(f'DELETE FROM produtos WHERE cod_prod = {cod_apagar}')
    connection.commit()

    print('''
        PRODUTO APAGADO COM SUCESSO!!!''')

#------------------------------------------------------------------------------------------------#
                                #MENU PARA ENTRAR NO LOOP
MENU = int(input('''
===================================================
¦                  BEM VINDO AO                   ¦
¦        SISTEMA DE CADASTRO DE PRODUTO!!!        ¦
===================================================
¦ OPÇÕES:                                         ¦
===================================================
¦ [1].CADASTRAR PRODUTO                           ¦
¦ [2].ALTERAR PRODUTO                             ¦
¦ [3].APAGAR PRODUTO                              ¦
¦ [4].MOSTRAR ESTOQUE                             ¦
¦ [0].SAIR                                        ¦                                                     
===================================================
                    OPÇÃO: '''))

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
 
        cursor.execute(f"INSERT INTO produtos VALUES ({cod_prod}, '{nome_prod}', '{desc_prod}', {CP}, {CF}, {CV}, {IV}, {ML})")
        connection.commit()

        os.system('cls')     
        
        CALCULO_TABELA()

        print('''
        PRODUTO CADASTRADO COM SUCESSO!!!''')
    elif(MENU==2): #ALTERAR PRODUTO
        ALTERAR_PRODUTO()
    elif(MENU==3): #APAGAR PRODUTO
        cod_apagar = int(input('Digite o codigo do produto que deseja apagar: '))
        sim_nao = str(input('CONFIRMAR A EXCLUSÃO DO PRODUTO <S/N>: ')).upper()

        while (sim_nao == 'N'):
            cod_apagar = int(input('Digite o codigo do produto que deseja apagar: '))
            sim_nao = str(input('CONFIRMAR A EXCLUSÃO DO PRODUTO <S/N>: ')).upper()

        cursor.execute(f'DELETE FROM produtos WHERE cod_prod = {cod_apagar}')
        connection.commit()

        print('''
        PRODUTO APAGADO COM SUCESSO!!!''')
    elif(MENU==4): #MOSTRAR ESTOQUE
        cursor.execute('SELECT * FROM produtos')
        print('''
        ESTOQUE COMPLETO DE PRODUTOS!!!''')
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

    MENU= int(input('''
                    
===================================================
¦            O QUE DESEJA FAZER AGORA?            ¦
===================================================
¦ OPÇÕES:                                         ¦
===================================================
¦ [1].CADASTRAR PRODUTO                           ¦
¦ [2].ALTERAR PRODUTO                             ¦
¦ [3].APAGAR PRODUTO                              ¦
¦ [4].MOSTRAR ESTOQUE                             ¦
¦ [0].SAIR                                        ¦
===================================================
                    OPÇÃO: '''))
    
    os.system('cls')

#------------------------------------------------------------------------------------------------#
                     #DESPEDIDA, ULTIMO COMMIT, TERMINAR CONEXAO E O CURSOR
print('TCHAU BRIGADO :) ')

connection.commit()
cursor.close()
connection.close()

#------------------------------------------------------------------------------------------------#

