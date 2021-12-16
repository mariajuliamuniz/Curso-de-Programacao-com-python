print("Um número é perfeito ou não?")
num=int(input("Digite um número inteiro: "))
i=1
soma=0
while (i<num):
    div=num%i
    if div==0:
        soma=soma+i
        print("Divisor:", i)
    i=i+1
if soma==num:
    print("O número", num,"é perfeito pois a soma de seus divisores é",soma,"que é igual ao número.")
else:
    print("O número",num,"não é perfeito.")
