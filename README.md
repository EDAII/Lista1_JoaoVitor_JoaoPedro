# Lista 1 -  EDA2 2019-1

## João Vitor Ramos de Souza e João Pedro Soares

### Do que se trata?
O programa oferece três análises diferentes de algorítmos de busca.

 - A **Opção 1** uma função de comparação de algorítimos de busca (sequencial, sequencial com sentinela, binária e busca sequencial em listas simplesmente encadeada e suplamente encadeadas) por tempo de execução(segundos) x tamanho do vetor. Ele executa 10 vezes, com um vetor desordenado, inicialmente com tamanho de 10000 elementos. Para adicionar aleatoriedade aos dados os algoritmos de busca possuem 80% de chance de serem escolhidos, já os de inserção e remoção possuem chance de 10% cada.
 **AVISO: Esta função demora alguns segundos para completar. O gráfico é exibido logo após o término da execução**
 
  - A **Opção 2** uma função de comparação de algorítimos de busca (sequencial, sequencial com sentinela, binária e busca sequencial em listas simplesmente encadeada e suplamente encadeadas) por tempo de execução(segundos) x tamanho do vetor. Ele executa 10 vezes, com um vetor desordenado, inicialmente com tamanho de 10000 elementos. Apenas realizando inserções na estrutura a cada iteração.
 **AVISO: Esta função demora alguns segundos para completar. O gráfico é exibido logo após o término da execução**

 - A **Opção 3** uma função de comparação de algorítimos de busca (sequencial, sequencial com sentinela, binária e busca sequencial em listas simplesmente encadeada e suplamente encadeadas) por tempo de execução(segundos) x tamanho do vetor. Ele executa 10 vezes, com um vetor desordenado, inicialmente com tamanho de 10000 elementos. Para adicionar aleatoriedade aos dados os algoritmos de busca possuem 20% de chance de serem escolhidos, já os de inserção e remoção possuem chance de 40% cada.
 **AVISO: Esta função demora alguns segundos para completar. O gráfico é exibido logo após o término da execução**

- A **Opção 4** é apenas a opção para sair do programa.


### Utilizando
#### Pré requisitos
Antes de utilizar o programa, você precisará do `matplotlib` e do `python3-tk`.

Em distribuições que utilizam o gerenciador de pacotes `apt`, utilize:

    $ sudo apt-get update
    $ sudo apt-get install pip3
    $ sudo apt-get install python3-tk 
    $ pip3 install matplotlib
    
#### Executando
Após o passo anterior, para executar o programa, navegue até o diretório raiz do programa e utilize:

    $ python3 main.py