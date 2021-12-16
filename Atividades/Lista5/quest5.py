nome = i = 0
lista_nome = []
primeiraletra = []
tamanho = []
while (nome!='FIM'):
    nome = input ("Digite vários nomes (FIM para parar): ")
    lista_nome.append(nome)
    letra = nome[0]
    primeiraletra.append(letra)
    tam = len(nome)
    tamanho.append(tam)
    i+=1
del lista_nome[-1]
print ("Palavras que você digitou, respectivamente: ",lista_nome)
del primeiraletra[-1]
print("Primeira letra de cada palavra, respectivamente:", primeiraletra)
del tamanho[-1]
print("Tamanho de cada palavra, respectivamente: ",tamanho)
