import random
import time

def busca_sequencial_sentinela(lista, elemento):
    """
    Reliza busca sequencial com sentinela do elemento passado por parametro
    lista -- lista de inteiros desordenada
    elemento -- elemento a ser buscado
    """
    contador = 0
    lista.append(contador)    
    try:        
        while lista[contador] != elemento:
            contador += 1
        if contador == len(lista) - 1:
            del lista[-1]
            return -1
        
        del lista[-1]
        return contador
    except IndexError:
        print('Elemento nao achado')


def insere_randomico(lista, qtd_insercao):
    """
    Insere n elementos de acordo com a quantidade passada por parametro
    qtd_insercao - quantidade a ser inserida na lista
    """
    for i in range(qtd_insercao):
        lista.append(random.randint(1,10000))
    random.shuffle(lista)
    return lista

def remove_randomico(lista, qtd_remocao):
    """
    Insere n elementos de acordo com a quantidade passada por parametro
    qtd_remocao - quantidade a ser removida na lista
    """
    for i in range(qtd_remocao):
        lista.pop(random.randrange(len(lista)))    
    return lista