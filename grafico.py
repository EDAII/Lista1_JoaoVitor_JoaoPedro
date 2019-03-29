import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

def plota_figura(time_results):
    print(time_results)
    fig = plt.figure()

    ax1 = fig.add_subplot(511)
    line1 = ax1.plot(np.linspace(6000, 15000, len(time_results['busca_binaria'])), time_results['busca_binaria'], 'bo-', label='binaria')
    ax1.tick_params(axis='both', which='major', labelsize=6)

    ax1.set_title('Tempo x Tamanho', fontsize=6)
    ax1.set_title('Tempo x Tamanho', fontsize=6)
    ax1.set_xlabel('distance (m)')

    ax2 = fig.add_subplot(512)
    line2 = ax2.plot(np.linspace(6000, 15000, len(time_results['busca_sequencial'])), time_results['busca_sequencial'], 'go-', label='sequencial')
    ax2.tick_params(axis='both', which='major', labelsize=6)

    ax3 = fig.add_subplot(513)
    line3 = ax3.plot(np.linspace(6000, 15000, len(time_results['busca_sequencial_sentinela'])), time_results['busca_sequencial_sentinela'], 'ro-', label='sequencial_sentinela')
    ax3.tick_params(axis='both', which='major', labelsize=6)

    ax4 = fig.add_subplot(514)
    line4 = ax4.plot(np.linspace(6000, 15000, len(time_results['busca_sequencial_encadeada'])), time_results['busca_sequencial_encadeada'], 'yo-', label='sequencial_encadeada')
    ax4.tick_params(axis='both', which='major', labelsize=6)

    ax5 = fig.add_subplot(515)
    line5 = ax5.plot(np.linspace(6000, 15000, len(time_results['busca_sequencial_duplamente_encadeada'])), time_results['busca_sequencial_duplamente_encadeada'], 'mo-', label='sequencial_duplamente_encadeada')
    ax5.tick_params(axis='both', which='major', labelsize=6)

    lines = line1 + line2 + line3 + line4 + line5
    labels = [l.get_label() for l in lines]

    ax5.legend(lines, labels, loc=(0,-0.5), ncol=5)

    plt.show()
