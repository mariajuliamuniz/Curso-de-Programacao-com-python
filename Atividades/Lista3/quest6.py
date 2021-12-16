print("Calcular a média de idades de um grupo")
print("Você pode digitar indeterminados dados até que um  valor negativo seja digitado.")
idade=0
contador=0
soma=0
while (idade>=0):
    contador = contador + 1
    idade=int(input('Digite a '+str(contador)+'ª idade:'))
    if idade >= 0:
        soma=idade+soma
contador=contador-1
media=soma/contador
print("Recebemos",contador,"idades.")
print("A média das idades é:",media)

