num = cont = 0
lista_num = []
while(num!=-1):
    num=int(input("Digite números inteiros (-1 para parar): "))
    lista_num.append(num)
    cont += 1
del lista_num[-1]
print(lista_num)
cont=cont-1
print(
    f"Valor mínimo: {min(lista_num)}\n"
    f"Valor máximo: {max(lista_num)}\n"
    f"Soma dos valores: {sum(lista_num)}\n"
    f"Média dos valores: {sum(lista_num)/cont}\n"
)