print("Digite DEZ números inteiros:")
i=0
lista_num = []
while(i<10):
    num = int(input("Digite um número: "))
    i+=1
    lista_num.append(num)
print("A lista que você digitou foi:", lista_num)  

j=0

newlista = []
while(j<10):
    mult = lista_num[j]*lista_num[j]
    newlista.append(mult) 
    j+=1
print("O quadrado dos compontentes da lista que você digitou é:", newlista)