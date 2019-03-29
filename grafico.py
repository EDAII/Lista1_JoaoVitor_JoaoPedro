import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

def plota_figura(resultado_busca, tamanho_listas):
    figura = plt.figure()

    ax1 = figura.add_subplot(511)
    line1 = ax1.plot(np.linspace(min(tamanho_listas["lista_vetor"]), max(tamanho_listas["lista_vetor"]), len(resultado_busca['busca_sequencial'])),
                    resultado_busca['busca_sequencial'], 'bo-', label='sequencial')
    ax1.tick_params(axis='both', which='major', labelsize=6)

    ax1.set_title('Tempo x Tamanho', fontsize=6)
    
    ax2 = figura.add_subplot(512)
    line2 = ax2.plot(np.linspace(min(tamanho_listas["lista_vetor"]), max(tamanho_listas["lista_vetor"]), len(resultado_busca['busca_sequencial_sentinela'])),
                     resultado_busca['busca_sequencial_sentinela'], 'go-', label='sequencial_sentinela')
    ax2.tick_params(axis='both', which='major', labelsize=6)

    ax3 = figura.add_subplot(513)
    line3 = ax3.plot(np.linspace(min(tamanho_listas["lista_vetor"]), max(tamanho_listas["lista_vetor"]), len(resultado_busca['busca_binaria'])),
                     resultado_busca['busca_binaria'], 'ro-', label='binaria')
    ax3.tick_params(axis='both', which='major', labelsize=6)

    ax4 = figura.add_subplot(514)
    line4 = ax4.plot(np.linspace(min(tamanho_listas["lista_vetor"]), max(tamanho_listas["lista_vetor"]), len(resultado_busca['busca_binaria'])),
                     resultado_busca['busca_sequencial_encadeada'], 'yo-', label='sequencial_encadeada')
    ax4.tick_params(axis='both', which='major', labelsize=6)

    ax5 = figura.add_subplot(515)
    line5 = ax5.plot(np.linspace(min(tamanho_listas["lista_vetor"]), max(tamanho_listas["lista_vetor"]), len(resultado_busca['busca_binaria'])),
                     resultado_busca['busca_sequencial_duplamente_encadeada'], 'mo-', label='sequencial_duplamente_encadeada')
    ax5.tick_params(axis='both', which='major', labelsize=6)

    lines = line1 + line2 + line3 + line4 + line5
    labels = [l.get_label() for l in lines]

    ax5.legend(lines, labels, loc=(0,-0.5), ncol=5)
    plt.show()

    
def plota_graficos_individuais(resultado_busca, tamanho_listas):
    plt.plot(np.linspace(min(tamanho_listas["lista_vetor"]), max(tamanho_listas["lista_vetor"]), len(resultado_busca['busca_sequencial'])),
                    resultado_busca['busca_sequencial'], 'bo-', label='sequencial')
    plt.legend()
    plt.show()

    plt.plot(np.linspace(min(tamanho_listas["lista_vetor"]), max(tamanho_listas["lista_vetor"]), len(resultado_busca['busca_sequencial_sentinela'])),
                    resultado_busca['busca_sequencial_sentinela'], 'go-', label='sequencial_sentinela')
    plt.legend()
    plt.show()

    plt.plot(np.linspace(min(tamanho_listas["lista_vetor"]), max(tamanho_listas["lista_vetor"]), len(resultado_busca['busca_binaria'])),
                    resultado_busca['busca_binaria'], 'ro-', label='binaria')
    plt.legend()
    plt.show()

    plt.plot(np.linspace(min(tamanho_listas["lista_vetor"]), max(tamanho_listas["lista_vetor"]), len(resultado_busca['busca_sequencial_encadeada'])),
                    resultado_busca['busca_sequencial_encadeada'], 'yo-', label='encadeada')
    plt.legend()
    plt.show()

    plt.plot(np.linspace(min(tamanho_listas["lista_vetor"]), max(tamanho_listas["lista_vetor"]), len(resultado_busca['busca_sequencial_duplamente_encadeada'])),
                    resultado_busca['busca_sequencial_duplamente_encadeada'], 'mo-', label='duplamente_encadeada')
    plt.legend()
    plt.show()