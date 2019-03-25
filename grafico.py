import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D


def plota_grafico_time_size(busca_binaria, busca_sequencial, busca_sentinela,lista_vetor):
    plt.ylabel('tempo(segundos)')
    plt.xlabel('tamanho')
    x = 
    
    plt.plot(busca_binaria,label='binaria', color='blue')
    plt.plot(busca_sequencial,label='sequencial', color='red')
    plt.plot(busca_sentinela, label='sentinela', color='green')

    plt.xticks(busca_, my_xticks)
    plt.yticks(np.arange(y.min(), y.max(), 0.005))
    plt.title('Tempo x Tamanho')
    plt.legend()
    # plt.xticks([9000,9500,10000,10500,11000])
    plt.show()

