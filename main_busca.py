import busca_binaria
import busca_sequencial
import busca_sequencial_sentinela
import linkedlist
import doublylinkedlist
import random
import time

if __name__ == "__main__":

    lista_vetor = random.sample(range(0,10 ** 4), 10 ** 4)
    lista_encadeada = linkedlist.LinkedList()
    lista_dupla_encadeada = doublylinkedlist.DoublyLinkedList()

    resultado_busca_binaria = []
    resultado_busca_sequencial = []
    resultado_busca_sequencial_sentinela = []
    resultado_lista_encadeada = []
    resultado_lista_duplamente_encadeada = []


    for i in range(10 ** 4):
        lista_dupla_encadeada.insert_at_front(random.randint(1, 11 ** 4))
        lista_encadeada.append(random.randint(1, 11 ** 4))
    for i in range(0,10):
        operation = random.randint(1,10)
        if 1 <= operation <= 8:
            elem = random.randint(1, 11 ** 4)
            
            # busca binaria
            start = time.time()
            lista_vetor = busca_binaria.bucket_sort(lista_vetor)
            busca_binaria.binary_search(lista_vetor, elem)
            end = time.time()
            elapsed_time = end - start
            resultado_busca_binaria.append(elapsed_time)
            print('resultado busca binaria\n', resultado_busca_binaria)

            # busca sequencial
            start = time.time()
            lista_vetor = busca_binaria.bucket_sort(lista_vetor)
            busca_binaria.binary_search(lista_vetor, elem)
            end = time.time()
            elapsed_time = end - start
            resultado_busca_sequencial.append(elapsed_time)
            print('resultado busca sequencial\n', resultado_busca_sequencial)

            # busca sequencial com sentinela
            start = time.time()
            lista_vetor = busca_binaria.bucket_sort(lista_vetor)
            busca_binaria.binary_search(lista_vetor, elem)
            end = time.time()
            elapsed_time = end - start
            resultado_busca_sequencial_sentinela.append(elapsed_time)
            print('resultado busca sequencial sentinela\n', resultado_busca_sequencial_sentinela)

            # lista encadeada busca sequencial
            start = time.time()
            lista_vetor = busca_binaria.bucket_sort(lista_vetor)
            busca_binaria.binary_search(lista_vetor, elem)
            end = time.time()
            elapsed_time = end - start
            resultado_lista_encadeada.append(elapsed_time)
            print('resultado busca sequencial lista encadeada\n', resultado_lista_encadeada)

            # lista duplamente encadeada busca sequencial
            start = time.time()
            lista_vetor = busca_binaria.bucket_sort(lista_vetor)
            busca_binaria.binary_search(lista_vetor, elem)
            end = time.time()
            elapsed_time = end - start
            resultado_lista_duplamente_encadeada.append(elapsed_time)
            print('resultado busca sequencial lista duplamente encadeada\n', resultado_lista_duplamente_encadeada)

        elif operation == 9:
            print('#'*100)
            print('Insere elementos nas listas')
            # busca sequencial, busca sequencial com sentinela e busca binária
            lista_vetor = busca_sequencial.insere_randomico(lista_vetor, 10 ** 3)

            # lista duplamente encadeada
            try:
                lista_dupla_encadeada.insert_n_nodes(random.randint(1, 10 ** 4),
                                                    random.randint(1, 11 ** 4), 10 ** 3)
            except ValueError:
                print('Chave não achada ao inserir na lista duplamente encadeada') 
            
            # lista encadeada
            lista_encadeada.insert_n_nodes(random.randint(1, 10 ** 4), random.randint(1, 11 ** 4), 10 ** 3)

        elif operation == 10:
            print('#'*100)
            print('Removendo elementos das listas')

            # busca sequencial, busca sequencial com sentinela e busca binária
            lista_vetor = busca_sequencial.remove_randomico(lista_vetor, 9 ** 3)

            # lista duplamente encadeada
            try:
                lista_dupla_encadeada.remove_n_nodes(random.randint(1, 9 ** 3), 10 ** 3)
            except ValueError:
                print('Chave não achada ao remover elemento da lista duplamente encadeada')

            #lista encadeada
            try:                
                lista_encadeada.remove_n_nodes(random.randint(1, 9 ** 3), 10 ** 3)
            except ValueError:
                print('Chave não achada aao remover elemento da lista encadeada')
                