print("Olá, vamos calcular o fatorial de um número inteiro e positivo.")
num=int(input("Digite um valor:"))
i=num-1
while (i>=1):
    num=num*i
    i=i-1
print("O fatorial é:",num)
