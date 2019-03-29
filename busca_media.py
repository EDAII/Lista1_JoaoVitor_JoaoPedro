import busca_binaria
import busca_sequencial
import busca_sequencial_sentinela
import lista_simplesmente_encadeada
import lista_duplamente_encadeada
import random
import time
from grafico import plota_figura, plota_graficos_individuais

def main():

    lista_vetor = random.sample(range(0,10 ** 3), 10 ** 3)
    lista_encadeada = lista_simplesmente_encadeada.ListaEncadeada()
    lista_dupla_encadeada = lista_duplamente_encadeada.ListaDuplamenteEncadeada()

    for i in range(0, 10001):
        lista_dupla_encadeada.insere_inicio(random.randint(1, 10 ** 3))
        lista_encadeada.append(random.randint(1, 10 ** 3))

    tempo_busca = {"busca_binaria": [],
                    "busca_sequencial": [],
                    "busca_sequencial_sentinela": [],
                    "busca_sequencial_encadeada": [],
                    "busca_sequencial_duplamente_encadeada": []}
    
    tamanho_listas = {"lista_vetor": [10 ** 3],
                      "lista_encadeada": [10 ** 3],
                      "lista_duplamente_encadeada": [10 ** 3]}
    

    for i in range(0,10):            
        elem = int(len(lista_vetor)/2)

        # Realiza busca sequencial
        inicio_cronometagem = time.time()
        busca_sequencial.busca_sequencial_index(lista_vetor, elem)
        fim_cronometragem = time.time()
        tempo_cronometragem = fim_cronometragem - inicio_cronometagem
        tempo_busca['busca_sequencial'].append(tempo_cronometragem)

        # Realiza busca sequencial com sentinela
        inicio_cronometagem = time.time()
        busca_sequencial_sentinela.busca_sequencial_sentinela(lista_vetor, elem)
        fim_cronometragem = time.time()
        tempo_cronometragem = fim_cronometragem - inicio_cronometagem
        tempo_busca['busca_sequencial_sentinela'].append(tempo_cronometragem)

        # Realiza busca binaria
        lista_vetor = busca_binaria.bucket_sort(lista_vetor)
        inicio_cronometagem = time.time()
        busca_binaria.binary_search(lista_vetor, elem)
        fim_cronometragem = time.time()
        tempo_cronometragem = fim_cronometragem - inicio_cronometagem
        tempo_busca['busca_binaria'].append(tempo_cronometragem)


        # Realiza busca sequencial na lista encadeada
        inicio_cronometagem = time.time()
        try:
            lista_encadeada.index(elem)
        except ValueError as exception:
            print(exception)            
        fim_cronometragem = time.time()
        tempo_cronometragem = fim_cronometragem - inicio_cronometagem
        tempo_busca['busca_sequencial_encadeada'].append(tempo_cronometragem)     

        # Realiza busca sequencial na lista duplamente encadeada 
        inicio_cronometagem = time.time()
        lista_dupla_encadeada.busca_sequencial(elem)
        fim_cronometragem = time.time()
        tempo_cronometragem = fim_cronometragem - inicio_cronometagem
        tempo_busca['busca_sequencial_duplamente_encadeada'].append(tempo_cronometragem)


        ###################INSERÇÃO##########################

        # Realiza insercao na lista de vetor
        crescimento = tamanho_listas["lista_encadeada"][-1] * 2
        lista_vetor = busca_sequencial.insere_randomico(lista_vetor, crescimento)
        tamanho_listas["lista_vetor"].append(tamanho_listas["lista_vetor"][-1] + crescimento)

        #Realiza insercao na lista duplamente encadeada
        try:
            lista_dupla_encadeada.insere_n_nos(crescimento)
            tamanho_listas["lista_duplamente_encadeada"].append(tamanho_listas["lista_duplamente_encadeada"][-1] + crescimento)
        except ValueError:
            print('Chave não achada ao inserir na lista duplamente encadeada') 
        
        # Realiza insercao na lista encadeada
        try:
            lista_encadeada.insere_n_nos(crescimento)
            tamanho_listas["lista_encadeada"].append(tamanho_listas["lista_encadeada"][-1] + crescimento)
        except IndexError:
            print('Chave não achada ao inserir na lista encadeada')
                
    plota_graficos_individuais(tempo_busca, tamanho_listas)
    plota_figura(tempo_busca, tamanho_listas)