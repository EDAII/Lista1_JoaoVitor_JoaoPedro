import random
import time

def busca_sequencial_sentinela(elementos_lista, elemento):    
    counter = 0
    elementos_lista.append(counter)    
    try:        
        while elementos_lista[counter] != elemento:
            counter += 1
        if counter == len(elementos_lista) - 1:
            del elementos_lista[-1]
            return -1
        
        del elementos_lista[-1]
        return counter
    except IndexError:
        print('Elemento nao achado')


def insere_randomico(lista, qtd_insercao):
    for i in range(qtd_insercao):
        lista.append(random.randint(1,10000))
    random.shuffle(lista)
    return lista

def remove_randomico(lista, qtd_remocao):
    for i in range(qtd_remocao):
        lista.pop(random.randrange(len(lista)))    
    return lista