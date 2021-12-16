print("Uma equação do segundo grau é do tipo Ax^2+Bx+C=0")
A=float(input("Digite o valor de A:"))
B=float(input("Digite o valor de B:"))
C=float(input("Digite o valor de C:"))
delta=B**2-4*A*C
if delta<0:
    print("A equação não possui raízes reais.")
elif delta>0:
    print("A equação possui duas raízes reais e distintas.")
    x1=(-B+delta**0.5)/(2*A)
    x2=(-B-delta**0.5)/(2*A)
    print("AS raízes da equação são:",x1,"e",x2)
else:
    print("A equação possui uma raiz real.")
    x=(-B)/(2*A)
    print("A raíz da equação é:",x)