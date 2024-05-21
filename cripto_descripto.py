alfanumerico = 'ZABCDEFGHIJKLMNOPQRSTUVWXY'
chave = [[4, 3], [1, 2]]
chave_inversa = [[42, -63], [-21, 84]]

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
                if [numero] == [indec]:
                    desc_cripto += alfanumerico[indec]
    return desc_cripto
def verificacao_para_criptografia(desc_prod): #VERIFICA SE A DESCRICAO É IMPAR
    if (len(desc_prod) % 2 != 0):
            desc_prod += desc_prod[-1]
    return desc_prod