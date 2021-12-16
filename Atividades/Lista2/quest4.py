print("Primeiro escolha uma opção e depois digite dois números")
print("1 – Soma de 2 Números")
print("2 -  Diferença entre 2 números (Maior pelo menor)")
print("3 – Produto entre 2 números")
print("4 – Divisão entre 2 números (denominador não pode ser zero)")
op=int(input("Opção:"))
num1=float(input("Digite o primeiro número:"))
num2=float(input("Digite o segundoo número:"))
if op==1:
    soma=num1+num2
    print("A soma entre os dois números é:",soma)
elif op==2:
    if num1>num2:
        dif=num1-num2
        print("A diferença entre os dois números é:", dif)
    elif num2>num1:
        dif = num2-num1
        print("A diferença entre os dois números é:", dif)
elif  op==3:
    prod=num1*num2
    print("O produto entre os dois números é:", prod)
elif op==4:
    if num1!=0.0:
        div=num2/num1
        print("A divisão entre o primeiro e segundo número é:",div)
    elif num2!=0.0:
        div = num1/num2
        print("A divisão entre o segundo e o primeiro número é:", div)
    elif (num1==0) and (num2==0):
        print("Divisão inválida!")
else:
    print("Opção inválida!")

