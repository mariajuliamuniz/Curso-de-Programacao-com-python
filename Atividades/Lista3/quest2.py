print("Por favor, digite 10 valores")
contador=soma=menor=maior=0

while (contador<10):
    contador=contador+1
    num=float(input('Digite o '+str(contador)+'º valor:'))
    soma=soma+num
    if contador==1:
        maior=menor=num
    else:
        if num>maior:
            maior=num
        if num<menor:
            menor=num

media=soma/10
print("A média dos números é:",media)
print("O maior é",maior)
print("O menor é",menor)
