def soma (n):
    soma = 0
    i =1
    while (i<=n):
        soma = soma + i
        i+=1
    print("A soma dos", n, "primeiros inteiros positivos é", soma)  

n = int(input("Digite o valor de n: "))   
soma(n)
