print("Vamos mostrar todos os divisores de um número inteiro.")
num=int(input("Digite um número:"))
i=1
while (i<=num):
    div=num%i
    if div==0:
        print("Divisor:",i)
    i=i+1

