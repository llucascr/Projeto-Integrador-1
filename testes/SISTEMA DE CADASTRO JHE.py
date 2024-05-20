import os
import oracledb
connection = oracledb.connect(user = "XXXXXXX", password = "XXXX", dsn = "172.16.12.14/xe")
cursor = connection.cursor()
#
alfanumerico = 'ZABCDEFGHIJKLMNOPQRSTUVWXY'
chave = [[4, 3], [1, 2]]
chave_inversa = [[42, -63], [-21, 84]]
#
def hill_criptografia(desc_prod, chave): #CRIPTOGRAFA E DESCRIPTOGRAFA
    numeros = [] #CONVERTE LETRA EM NUMERO
    for index in range(len(desc_prod)):
        for indec in range(len(alfanumerico)):
            if desc_prod[index] == alfanumerico[indec]:
                numeros.append(indec)
    #
    parNumeros = [] #SEPARA OS NUMEROS EM PARES
    for i in range(0, len(numeros), 2):
        parNumeros.append(numeros[i:i+2])
    #
    multi = [] #MULTIPLICA OS NUMEROS PELA CHAVE
    for par in parNumeros:
        soma = 0
        soma = [(((chave[0][0] * par[0]) + (chave[0][1] * par[1])) % 26), 
                (((chave[1][0] * par[0]) + (chave[1][1] * par[1])) % 26)]
        multi.append(soma)
    #
    desc_cripto = '' #CONVERTE NUMERO EM LETRA
    for index in multi:
        for numero in index:
            for indec in range(len(alfanumerico)):
                if [numero] == [index]:
                    desc_cripto += alfanumerico[indec]
    return desc_cripto
def verificacao_para_criptografia(desc_prod): #VERIFICA SE A DESCRICAO É IMPAR
    if (len(desc_prod) % 2 != 0):
            desc_prod += desc_prod[-1]
    return desc_prod
def verificacao_para_descriptografia(desc_prod): #VERIFICA SE AS DUAS LETRAS FINAIS DA DESCRICAO DESCRIPTOGRAFADA SAO IGUAIS E RETIRA A ULTIMA
    if desc_prod[-1] == desc_prod[-2]:
        desc_prod = desc_prod[:-1]
    return desc_prod
#
def calculo_print_tabela(cod_prod, nome_prod, desc_prod, CP, CF, CV, IV, ML): #CALCULA E IMPRIME A TABELA
    PV = CP/(1-((CF+CV+IV+ML)/100)) #CALCULAR O VALOR PARA VENDA DO PRODUTO
    #
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
    #
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
    #
    print(f'''                      
=========================================================
 CÓDIGO: {cod_prod}\t\t\t\t\t\t
 PRODUTO: {nome_prod}\t\t\tVALOR\t  %
 DESCRIÇÃO: {desc_prod}\t\t\t\t\t\t           
=========================================================
 A. Preço de Venda\t\t¦ R${PV:.2f}\t¦  100%\t
 B. Custo de Aquisição\t\t¦ R${CP:.2f}\t¦  {CPpor:.0f}% \t
 C. Receita Bruta(A-B)\t\t¦ R${RBnum:.2f}\t¦  {RBpor:.0f}% \t
 D. Custo Fixo/Administrativo\t¦ R${CFnum:.2f}\t¦  {CF:.0f}% \t                   
 E. Comissão de Vendas\t\t¦ R${CVnum:.2f}\t¦  {CV:.0f}% \t
 F. Impostos\t\t\t¦ R${IVnum:.2f}\t¦  {IV:.0f}% \t
 G. Outros Custos(D+E+F)\t¦ R${OCnum:.2f}\t¦  {OCpor:.0f}% \t
 H. Rentabilidade(C-G)\t\t¦ R${Rnum:.2f}\t¦  {Rpor:.0f}% \t
=========================================================
 CLASSIFICAÇÃO DE LUCRO:\t {ClassLucro}\t\t
=========================================================
        ''')
#
def cadastrar_produto():
    cod_prod = int(input('CÓDIGO DO PRODUTO: '))             #CODIGO DO PRODUTO
    nome_prod = str(input('NOME DO PRODUTO: '))              #NOME DO PRODUTO
    desc_prod = str(input('DESCRIÇÃO DO PRODUTO: ')).upper() #DESCRIÇÃO DO PRODUTO
    CP = float(input('CUSTO DO PRODUTO: '))                  #CUSTO PAGO PELO PRODUTO PARA O FORNECEDOR
    CF = float(input('CUSTO FIXO/ADMINISTRATIVO(%): '))      #CUSTO FIXO (ESPAÇO FÍSICO, DESPESAS, FUNCIONÁRIOS...)
    CV = float(input('COMISSÃO DE VENDAS: '))                #COMISSÃO SOBRE A VENDA DO PRODUTO
    IV = float(input('IMPOSTOS(%): '))                       #IMPOSTOS SOBRE A VENDA DO PRODUTO
    ML = float(input('MARGEM DE LUCRO DO PRODUTO: '))        #MARGEM DE LUCRO SOBRE A VENDA DO PRODUTO
    #
    calculo_print_tabela(cod_prod, nome_prod, desc_prod, CP, CF, CV, IV, ML)
    #
    desc_prod = verificacao_para_criptografia(desc_prod)
    desc_cripto = hill_criptografia(desc_prod, chave)
    #
    cursor.execute(f"INSERT INTO ESTOQUE VALUES ({cod_prod}, '{nome_prod}', '{desc_cripto}', {CP}, {CF}, {CV}, {IV}, {ML})")    
    connection.commit()
    #
    print('--->>> PRODUTO CADASTRADO COM SUCESSO!!! <<<---')
def alterar_produto():
    cod_prod = int(input('CÓDIGO DO PRODUTO: '))
    #
    cursor.execute(f'SELECT * FROM ESTOQUE WHERE COD_PROD = {cod_prod}')
    row = cursor.fetchone()
    #
    if (row):
        menu_alteracao = int(input('''
===================================================
¦               O QUE DESEJA ALTERAR:             ¦
===================================================
¦ [1].NOME DO PRODUTO    ¦ [5].CUSTO FIXO         ¦
¦ [2].DESCRIÇÃO PRODUTO  ¦ [6].COMISSÃO DE VENDAS ¦
¦ [3].CUSTO DO PRODUTO   ¦ [7].IMPOSTOS           ¦
¦ [4].MARGEM DE LUCRO    ¦                        ¦
===================================================
                    OPÇÃO: '''))
        #
        alteracao = str(input('NOVO VALOR PARA O CAMPO: '))
        #
        if (menu_alteracao == 1):
            cursor.execute(f"UPDATE ESTOQUE SET nome_prod = '{alteracao}' WHERE COD_PROD = {cod_prod}")
        #
        elif (menu_alteracao == 2):
            alteracao = verificacao_para_criptografia(alteracao)
            desc_cripto = hill_criptografia(alteracao, chave)
            cursor.execute(f"UPDATE ESTOQUE SET desc_prod = '{desc_cripto}' WHERE COD_PROD = {cod_prod}")
        #
        elif (menu_alteracao == 3):
            cursor.execute(f'UPDATE ESTOQUE SET cp = {alteracao} WHERE COD_PROD = {cod_prod}')
        elif (menu_alteracao == 4):
            cursor.execute(f'UPDATE ESTOQUE SET ml = {alteracao} WHERE COD_PROD = {cod_prod}')
        elif (menu_alteracao == 5):
            cursor.execute(f'UPDATE ESTOQUE SET cf = {alteracao} WHERE COD_PROD = {cod_prod}')
        elif (menu_alteracao == 6):
            cursor.execute(f'UPDATE ESTOQUE SET cv = {alteracao} WHERE COD_PROD = {cod_prod}')
        elif (menu_alteracao == 7):
            cursor.execute(f'UPDATE ESTOQUE SET iv = {alteracao} WHERE COD_PROD = {cod_prod}')
        #
        connection.commit()
        #
        print('--->>> PRODUTO ALTERADO COM SUCESSO!!! <<<---')
        #   
    else:
        print('--->>> CODIGO INVALIDO!!! <<<---')    
def apagar_produto():
    cod_prod = int(input('CÓDIGO DO PRODUTO: '))
    #
    cursor.execute(f'SELECT * FROM ESTOQUE WHERE COD_PROD = {cod_prod}')
    row = cursor.fetchone()
    #
    if (row):
        desc_prod = hill_criptografia(row[2], chave_inversa)
        desc_prod = verificacao_para_descriptografia(desc_prod)
        #
        calculo_print_tabela(row[0], row[1], desc_prod, row[3], row[4], row[5], row[6], row[7])
        #
        sim_nao = str(input('CONFIRMAR A EXCLUSÃO DO PRODUTO <S/N>: ')).upper()
        if (sim_nao == 'S'):
            cursor.execute(f'DELETE FROM ESTOQUE WHERE COD_PROD = {cod_prod}')
            #
            connection.commit()
            #
            print('--->>> PRODUTO APAGADO COM SUCESSO!!! <<<---')
    else:
        print('--->>> CODIGO INVALIDO!!! <<<---')
def mostrar_estoque():
    cursor.execute('SELECT * FROM ESTOQUE')
    #
    print('--->>> ESTOQUE COMPLETO DE PRODUTOS!!! <<<---')
    #
    for row in cursor:
        #
        desc_prod = hill_criptografia(row[2], chave_inversa)
        desc_prod = verificacao_para_descriptografia(desc_prod)
        #
        calculo_print_tabela(row[0], row[1], desc_prod, row[3], row[4], row[5], row[6], row[7])
#
os.system('cls')
MENU = int(input('''
===================================================
¦                  BEM VINDO AO                   ¦
¦        SISTEMA DE CADASTRO DE PRODUTO!!!        ¦
===================================================
¦ [1].CADASTRAR PRODUTO                           ¦
¦ [2].ALTERAR PRODUTO                             ¦
¦ [3].APAGAR PRODUTO                              ¦
¦ [4].MOSTRAR ESTOQUE                             ¦
¦ [0].SAIR                                        ¦
===================================================
                    OPÇÃO: '''))
os.system('cls')
#
while (MENU != 0):
    if  (MENU == 1): #CADASTRAR PRODUTO
        cadastrar_produto()
    elif (MENU == 2): #ALTERAR PRODUTO
        alterar_produto()
    elif (MENU == 3): #APAGAR PRODUTO
        apagar_produto()
    elif (MENU == 4): #MOSTRAR ESTOQUE
        mostrar_estoque()
    MENU = int(input('''
                     
===================================================
¦          SISTEMA DE CADASTRO DE PRODUTO         ¦
===================================================
¦ [1].CADASTRAR PRODUTO                           ¦
¦ [2].ALTERAR PRODUTO                             ¦
¦ [3].APAGAR PRODUTO                              ¦
¦ [4].MOSTRAR ESTOQUE                             ¦
¦ [0].SAIR                                        ¦
===================================================
                    OPÇÃO: '''))
    os.system('cls')
#
print('--->>> OBRIGADA POR USAR O SISTEMA!!! <<<---')
connection.commit()
cursor.close()
connection.close()
