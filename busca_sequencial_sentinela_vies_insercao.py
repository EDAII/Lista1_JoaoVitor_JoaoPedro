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

def main():
    lista = random.sample(range(0,10 ** 4), 10 ** 4)
    for i in range(0,20):
        operation = random.randint(1,10)        
        if 9 <= operation <=10:
            print('#'*100)
            print('Realiza busca sequencial')
            elem = random.randint(1, 11 ** 4)
            print('Tamanho lista:',len(lista))
            print('Elemento procurado:',elem)
            start = time.time()
            busca_sequencial_sentinela(lista, elem)
            end = time.time()
            elapsed_time = end - start
            print('Tempo para realizar busca sequencial:', elapsed_time)
        elif 1 <= operation <= 4:
            print('#'*100)
            print('Insere elementos da lista')
            lista = insere_randomico(lista, 10 ** 3)
        elif 5 <= operation <= 8:
            print('#'*100)
            print('Removendo elementos da lista')
            lista = remove_randomico(lista, 9 ** 3)

main()
