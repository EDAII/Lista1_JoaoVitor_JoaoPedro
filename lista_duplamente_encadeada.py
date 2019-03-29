# Python implementation of Doubly linked list 
import sys
import random
import time

class No:
    def __init__(self, dado):
        self.dado = dado
        self.prox = None
        self.ant = None

class ListaDuplamenteEncadeada:
    def __init__(self):
        self.inicio = None 
        self.fim = None


    def insere_inicio(self, valor):
        """
        Insere valor no início  da lista
        """
        no = No(valor)
        if self.esta_vazia():
            self.inicio = no
            self.fim = no
        else:
            no.prox = self.inicio
            self.inicio.ant = no
            self.inicio = no

     
    def insert_at_back(self, valor):
        """
        Insere valor no final da lista
        """
        node = No(valor)
        if self.esta_vazia():
            self.inicio = node
        else:
           self.fim.prox = node
           node.ant = self.fim
           self.fim = node
    

    def insere_depois_no(self, chave, valor):
        """
        Insere valor após nó
        """
        no = No(valor)

        # Encontra posição da chave
        atual = self.inicio
        while atual != None and atual.dado != chave:
            atual = atual.prox

        if atual == None:
            raise ValueError('Chave não achada')

        if atual.prox == None:
            atual.prox = no
            no.ant = atual
            self.fim = no 
        else:
            prox_no = atual.prox
            atual.prox = no
            no.ant = atual
            no.prox = prox_no
            prox_no.ant = no

    def primeiro_no(self):
        """
        Retorna o dado do primeiro nó da lista
        """
        if self.esta_vazia():
            print('Lista está vazia')
            return

        return self.inicio.dado


    def ultimo_no(self):
        """
        Retorna o dado do último nó da lista
        """
        if self.esta_vazia():
            print('List is empty')
            return

        atual = self.inicio
        while atual.prox != None:
            atual = atual.prox

        return atual.dado


    def pop_primeiro_no(self):
        """
        Remove o primeiro nó da lista e retorna item
        """
        if self.esta_vazia():
            print('Lista está vazia')
            return

        prox_no = self.inicio.prox
        if (prox_no != None):
            prox_no.ant = None
        item = self.inicio.dado
        self.inicio = prox_no
        return item


    def pop_ultimo_no(self):
        """
        Remove o último nó da lista e retorna item
        """
        if self.esta_vazia():
            print('Lista está vazia')
            return

        item = self.fim.dado
        ant = self.fim.ant

        if ant != None:
            ant.prox = None

        self.fim.ant = None
        self.fim = ant

        return item


    def remove(self, chave):
        """
        Remove um item com o valor passado pelo parâmetro chave
        """
        if self.esta_vazia():
            print('List is empty')
            return

        atual = self.inicio

        while atual != None and atual.dado != chave:
            atual = atual.prox

        if atual == None:
            raise ValueError('Chave não achada')

        # Se atual está no inicio, deleta inicio
        if atual.ant == None:
            self.pop_primeiro_no()
        elif atual.prox == None: # Se atual é o último item
            self.pop_ultimo_no()
        else: # qualquer lugar entre o início e o fim da lista
            prox_no = atual.prox
            prev_node = atual.ant

            prev_node.prox = prox_no
            prox_no.ant = prev_node

            atual.prox = None 
            atual.ant = None
            atual = None


    def busca_sequencial(self, chave):
        """
        Busca se a chave está na lista
        """
        if self.esta_vazia():
            print('Lista está vazia')
            return False

        atual = self.inicio
        while atual != None and atual.dado != chave:
            atual = atual.prox

        if atual == None:
            return False

        return True


    def esta_vazia(self):
        """
        Checa se a lista está vazia
        """
        return self.inicio == None

    
    def print_lista(self):
        """
        Printa toda a lista
        """
        if self.esta_vazia():
            print("Nada a ser mostrado")
        else:
            atual = self.inicio
            while (atual != None):
                sys.stdout.write(str(atual.dado) + ' ')
                atual = atual.prox

            print('')
    
    def print_reverse(self):
        """
        Printa a lista de tras para a frente
        """
        if self.esta_vazia():
            print("Nada a ser mostrado")
        else:
            atual = self.fim
            while (atual != None):
                sys.stdout.write(str(atual.dado) + ' ')
                atual = atual.ant
    
            print('')
	
    def insere_n_nos(self, num_nos):
        """
        Insere um numero de n nós
        """
        for i in range(num_nos):
            elem = random.randint(1, 11 ** 4)
            index = random.randint(1, 11 ** 4)
            self.insere_depois_no(index, elem)

    def remove_n_nos(self, num_nos):
        """
        Remove um número de n nós
        """
        for i in range(num_nos):
            elem = random.randint(1, 11 ** 4)
            self.remove(elem)