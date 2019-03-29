import random
import time

def busca_sequencial(elementos_lista, elemento):
    i = 0
    try:
        while i <= len(elementos_lista):
            if elementos_lista[i] == elemento:
                break
            i += 1
        return i
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
