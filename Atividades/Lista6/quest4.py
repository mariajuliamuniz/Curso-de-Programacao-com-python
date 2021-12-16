def soma (x,y):
    soma = x + y
    print("A soma dos números é ", soma)

def subt (x,y):
    if (x>y):
        subt = x -y
    else:
        subt = y-x
    print("A subtração entre os números (maior - menor) é ", subt)

def mult (x,Y):
    mult = x*y
    print("A multplicação entre os números é ", mult)

def div (x,y):
    if (y!=0.0)and(x!=0.0):
        div1=x/y
        div2=y/x
        print("A divisão entre o primeiro e segundo número é:",div1)
        print("A divisão entre o segundo e o primeiro número é:", div2)
    elif x!=0.0:
        div = y/x
        print("A divisão entre o segundo e o primeiro número é:", div)
    elif y!=0.0:
        div = x/y
        print("A divisão entre o primeiro e segundo número é:", div)
    elif (x==0) and (x==0):
        print("Divisão inválida!")


print("Digite dois números:")
x = float(input("número x: "))
y = float(input("número y: "))
soma (x,y)
subt (x,y)
mult (x,y)
div (x,y)
