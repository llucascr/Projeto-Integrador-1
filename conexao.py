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
        # pv = estoque[3] / (1 - ((estoque[4] + estoque[5] + estoque[6] + estoque[7]) / 100))

        # # ---------------------------- CALCULOS DOS VALORES -----------------------------
        # # 'porc' = porcentagem
        # # 'valor' = variaveis float
        # porc_aquisicao = (estoque[3] * 100) / pv                            # LINHA B

        # receita_bruta = pv - estoque[3]                                     # LINHA C
        # valor_rb = pv - estoque[3]
        # porc_c = 100 - porc_aquisicao

        # valor_cf = (pv * estoque[4]) / 100       #cf                            # LINHA D
        # valor_cv = (pv * estoque[5]) / 100       #cv                            # LINHA E
        # valor_iv = (pv * estoque[6]) / 100       #iv                            # LINHA F

        # outros = valor_cf + valor_cv + valor_iv                           # LINHA G
        # porc_outros = estoque[4] + estoque[5] + estoque[6]
        
        # valor_rt = valor_rb - outros                                      # LINHA H
        # # Porcentual de Rentabilidade
        # porc_rt = porc_c - porc_outros
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
                 ESTOQUE DE PRODUTOS!!!
=================================================================
¦ CÓDIGO PRODUTO: {cod_prod}    \t\t¦\t\t¦\t\t¦
¦ PRODUTO: {nome_prod}    \t\t¦\tVALOR\t¦\t%\t¦
¦ DESCRIÇÃO: {desc_prod}    \t\t¦\t\t¦\t\t¦           
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


# [4] DELETAR TABELA
def deletar_tabela():
    cursor.execute(f"DROP TABLE PRODUTOS")

# [5] DELETAR PRODUTO
def deletar_produto():
    cursor.execute("DELETE FROM PRODUTOS")

# cursor.execute ("INSERT INTO PRODUTOS VALUES (1, 'Lapis', 'Preto', 1.00, 10, 5, 18, 25)")
# cursor.execute ("INSERT INTO PRODUTOS VALUES (2, 'Lapis', 'Amarelo', 1.20, 10, 5, 18, 25)")
# cursor.execute ("INSERT INTO PRODUTOS VALUES (3, 'Lapis', 'Chines', 0.20, 10, 5, 18, 0)")