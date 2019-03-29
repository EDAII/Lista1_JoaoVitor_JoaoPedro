import random
import time

def busca_sequencial(lista, elemento):
    """
    Realiza busca sequencial do elemento passado por parametro
    lista -- lista de inteiros desordenada
    elemento -- elemento a ser buscado
    """
    contador = 0
    try:
        while contador <= len(lista):
            if lista[contador] == elemento:
                break
            contador += 1
        return contador
    except IndexError:
        print('Elemento nao achado')

def busca_sequencial_index(lista, elemento):
    """
    Realiza busca sequencial do elemento passado por parametro
    lista -- lista de inteiros desordenada
    elemento -- elemento a ser buscado
    """
    contador = 0
    try:
        while contador <= len(lista):
            if contador == elemento:
                break
            contador += 1
        print('SEQUENCIAL INDEX DEU CERTO')
        return contador
    except IndexError:
        print('Elemento nao achado')

def insere_randomico(lista, qtd_insercao):
    """
    Insere n elementos de acordo com a quantidade passada por parametro
    qtd_insercao -- quantidade a ser inserida na lista
    """
    for contador in range(qtd_insercao):
        lista.append(random.randint(1,10000))
    random.shuffle(lista)
    return lista

def remove_randomico(lista, qtd_remocao):
    """
    Insere n elementos de acordo com a quantidade passada por parametro
    qtd_remocao -- quantidade a ser removida na lista
    """
    print(len(lista))
    for contador in range(qtd_remocao):
        lista.pop(random.randrange(len(lista)))    
    return lista
