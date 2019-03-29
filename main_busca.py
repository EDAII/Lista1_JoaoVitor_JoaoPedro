import busca_binaria
import busca_sequencial
import busca_sequencial_sentinela
import linkedlist
import doublylinkedlist
import random
import time
import main_insercao
from grafico import plota_figura

if __name__ == "__main__":

    lista_vetor = random.sample(range(0,10 ** 4), 10 ** 4)
    lista_encadeada = linkedlist.LinkedList()
    lista_dupla_encadeada = doublylinkedlist.DoublyLinkedList()

    for i in range(0, 10001):
        lista_dupla_encadeada.insert_at_front(random.randint(1, 11 ** 4))
        lista_encadeada.append(random.randint(1, 11 ** 4))

    time_results = {"busca_binaria": [],
                    "busca_sequencial": [],
                    "busca_sequencial_sentinela": [],
                    "busca_sequencial_encadeada": [],
                    "busca_sequencial_duplamente_encadeada": []}
    

    for i in range(0,10):
        operation = random.randint(1,10)
        if 1 <= operation <= 8:
            elem = random.randint(1, 11 ** 4)
            

            # busca sequencial
            start = time.time()
            busca_sequencial.busca_sequencial(lista_vetor, elem)
            end = time.time()
            elapsed_time = end - start
            time_results['busca_sequencial'].append(elapsed_time)

            # busca sequencial com sentinela
            start = time.time()
            busca_sequencial_sentinela.busca_sequencial_sentinela(lista_vetor, elem)
            end = time.time()
            elapsed_time = end - start
            time_results['busca_sequencial_sentinela'].append(elapsed_time)

            # busca binaria
            lista_vetor = busca_binaria.bucket_sort(lista_vetor)
            start = time.time()
            busca_binaria.binary_search(lista_vetor, elem)
            end = time.time()
            elapsed_time = end - start
            time_results['busca_binaria'].append(elapsed_time)


            # lista encadeada busca sequencial
            start = time.time()
            try:
                lista_encadeada.index(elem)
            except ValueError as exception:
                print(exception)
            
            end = time.time()
            elapsed_time = end - start
            time_results['busca_sequencial_encadeada'].append(elapsed_time)     

            # lista duplamente encadeada busca sequencial
            start = time.time()
            lista_dupla_encadeada.find(elem)
            end = time.time()
            elapsed_time = end - start
            time_results['busca_sequencial_duplamente_encadeada'].append(elapsed_time)

        elif operation == 9:
            # busca sequencial, busca sequencial com sentinela e busca binária
            len_vetor = len(lista_vetor)            
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
            
    plota_figura(time_results)

main_insercao.main()