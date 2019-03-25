import random
import time


def bucket_sort(alist):
    largest = max(alist)
    length = len(alist)
    size = largest/length
 
    buckets = [[] for _ in range(length)]
    for i in range(length):
        j = int(alist[i]/size)
        if j != length:
            buckets[j].append(alist[i])
        else:
            buckets[length - 1].append(alist[i])
 
    for i in range(length):
        insertion_sort(buckets[i])
 
    result = []
    for i in range(length):
        result = result + buckets[i]
 
    return result
 
def insertion_sort(alist):
    for i in range(1, len(alist)):
        temp = alist[i]
        j = i - 1
        while (j >= 0 and temp < alist[j]):
            alist[j + 1] = alist[j]
            j = j - 1
        alist[j + 1] = temp

def binary_search(a_list, item):
    """Performs iterative binary search to find the position of an integer in a given, sorted, list.

    a_list -- sorted list of integers
    item -- integer you are searching for the position of
    """

    first = 0
    last = len(a_list) - 1

    while first <= last:
        i = int((first + last) / 2)

        if a_list[i] == item:
            return i
        elif a_list[i] > item:
            last = i - 1
        elif a_list[i] < item:
            first = i + 1
        else:
            return '{item} nao achado na lista'.format(item=item)
 
def insere_randomico(lista, qtd_insercao):
    for i in range(qtd_insercao):
        lista.append(random.randint(1,10000))
    random.shuffle(lista)
    return lista

def remove_randomico(lista, qtd_remocao):
    for i in range(qtd_remocao):
        lista.pop(random.randrange(len(lista)))    
    return lista

# def main():
#     lista = random.sample(range(0,10 ** 4), 10 ** 4)
#     for i in range(0,20):
#         operation = random.randint(1,10)
#         if 9 <= operation <= 10:
#             print('#'*100)
#             print('Realiza busca sequencial')
#             elem = random.randint(1, 11 ** 4)
#             print('Tamanho lista:',len(lista))
#             print('Elemento procurado:',elem)
#             start = time.time()
#             lista = bucket_sort(lista)
#             binary_search(lista, elem)
#             end = time.time()
#             elapsed_time = end - start
#             print('Tempo para realizar busca binaria:', elapsed_time)
#         elif 1 <= operation <= 4:
#             print('#'*100)
#             print('Insere elementos da lista')
#             lista = insere_randomico(lista, 10 ** 3)
#         elif 5 <= operation <= 8:
#             print('#'*100)
#             print('Removendo elementos da lista')
#             lista = remove_randomico(lista, 9 ** 3)

# main()
