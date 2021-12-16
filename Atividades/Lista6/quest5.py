import random
def aleatoria ():

    lista_aleatoria = []
    i = len(lista_aleatoria)
    
    while (i<12):
        x = random.randint(10, 40)
        lista_aleatoria.append(x)
        listafinal = (set(lista_aleatoria))
        i=len(listafinal)
    print (listafinal)

aleatoria()