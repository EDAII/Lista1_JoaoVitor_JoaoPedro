import random
import time


def bucket_sort(lista):
    """
    Realiza ordenacao utilizando bucket sort
    lista -- lista de inteiros desordenados
    """
    maior = max(lista)
    tamanho_lista = len(lista)
    size = maior/tamanho_lista
 
    buckets = [[] for _ in range(tamanho_lista)]
    for i in range(tamanho_lista):
        if size == 0:
            raise ValueError("Lista esta vazia")
        j = int(lista[i]/size)
        if j != tamanho_lista:
            buckets[j].append(lista[i])
        else:
            buckets[tamanho_lista - 1].append(lista[i])
 
    for i in range(tamanho_lista):
        insertion_sort(buckets[i])
 
    result = []
    for i in range(tamanho_lista):
        result = result + buckets[i]
 
    return result
 
def insertion_sort(lista):
    """
    Realiza ordenação utilizando insertion sort
    lista -- lista de inteiros desordenados    
    """
    for i in range(1, len(lista)):
        temp = lista[i]
        j = i - 1
        while (j >= 0 and temp < lista[j]):
            lista[j + 1] = lista[j]
            j = j - 1
        lista[j + 1] = temp

def binary_search(lista, item):
    """
    Realiza busca binaria para achar a posicao do inteiro passado em uma lista ordenada
    lista -- lista de inteiros ordenados
    item -- inteiro a ser buscado
    """
    primeiro = 0
    ultimo = len(lista) - 1

    while primeiro <= ultimo:
        i = int((primeiro + ultimo) / 2)

        if lista[i] == item:
            return i
        elif lista[i] > item:
            ultimo = i - 1
        elif lista[i] < item:
            primeiro = i + 1
        else:
            return '{item} nao achado na lista'.format(item=item)
 
def insere_randomico(lista, qtd_insercao):
    """
    Insere n elementos de acordo com a quantidade passada por parametro
    qtd_insercao -- quantidade a ser inserida da lista
    """
    for i in range(qtd_insercao):
        lista.append(random.randint(1,10000))
    random.shuffle(lista)
    return lista

def remove_randomico(lista, qtd_remocao):
    """
    Remove n elementos de acordo com a quantidade passada por parametro
    qtd_remocao -- quantidade a ser removida da lista
    """
    for i in range(qtd_remocao):
        lista.pop(random.randrange(len(lista)))    
    return lista