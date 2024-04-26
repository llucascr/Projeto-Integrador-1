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
        connection.commit()
        estoque = row

        #------------------------------------------------------------------------------------------------------------------------#
                                              #CALCULOS DO PRODUTO
        cod_prod = estoque[0]
        nome_prod = estoque[1]
        desc_prod = estoque[2]
        CP = estoque[3]
        CF = estoque[4]
        CV = estoque[5]
        IV = estoque[6]
        ML = estoque[7]
        
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
        #------------------------------------------------------------------------------------------------------------------------#
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
        #------------------------------------------------------------------------------------------------------------------------#
                                        #IMPRIMINDO TABELA COM O CALCULO DO PRODUTO            
        print(f'''
                 
=================================================================
¦ CÓDIGO: {cod_prod}\t\t\t\t\t\t
¦ PRODUTO: {nome_prod}\t\t\tVALOR\t\t%\t
¦ DESCRIÇÃO: {desc_prod}\t\t\t\t\t\t           
=================================================================
¦ A. Preço de Venda\t\t¦ R${PV:.2f}\t¦  100%\t\t¦
¦ B. Custo de Aquisição\t\t¦ R${CP:.2f}\t¦  {CPpor:.0f}%\t\t¦    
¦ C. Receita Bruta(A-B)\t\t¦ R${RBnum:.2f}\t¦  {RBpor:.0f}%\t\t¦  
¦ D. Custo Fixo/Administrativo\t¦ R${CFnum:.2f}\t¦  {CF:.0f}%\t\t¦                     
¦ E. Comissão de Vendas\t\t¦ R${CVnum:.2f}\t¦  {CV:.0f}%\t\t¦
¦ F. Impostos\t\t\t¦ R${IVnum:.2f}\t¦  {IV:.0f}%\t\t¦
¦ G. Outros Custos(D+E+F)\t¦ R${OCnum:.2f}\t¦  {OCpor:.0f}%\t\t¦
¦ H. Rentabilidade(C-G)\t\t¦ R${Rnum:.2f}\t¦  {Rpor:.0f}%\t\t¦
=================================================================
¦ CLASSIFICAÇÃO DE LUCRO:\t {ClassLucro}\t\t\t¦
=================================================================

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
    connection.commit()

# [3] DELETAR TABELA
def deletar_tabela():
    cursor.execute(f"DROP TABLE PRODUTOS")
    connection.commit()

# [4] DELETAR PRODUTO
def deletar_produto():
    cursor.execute("DELETE FROM PRODUTOS")
    connection.commit()
