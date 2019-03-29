import random
import time

class No:
    def __init__(self, dado):
        self.dado = dado
        self.prox = None

class ListaEncadeada:
    def __init__(self):
        self.inicio = None
        self._size = 0
    
    def append(self, elem):
        """
        Adiciona um novo elemento após a última posição da lista
        """
        if self.inicio:
            # inserção quando a lista já possui elementos
            ponteiro = self.inicio
            while(ponteiro.prox):
                ponteiro = ponteiro.prox
            ponteiro.prox = No(elem)
        else:
            # primeira inserção
            self.inicio = No(elem)
        self._size = self._size + 1

    def _pega_no(self, index):
        """
        Retorna um no de acordo com a posicao passada por parametro
        """
        ponteiro = self.inicio
        for i in range(index):
            if ponteiro:
                ponteiro = ponteiro.prox
            else:
                raise IndexError("list index out of range")
        return ponteiro


    def __len__(self):
        """"
        Retorna o tamanho da lista
        """
        return self._size

    def __getitem__(self, index):        
        # a = lista[i]
        ponteiro = self._pega_no(index)
        if ponteiro:
            return ponteiro.dado
        raise IndexError("list index out of range")

    def __setitem__(self, index, elem):
        # lista[i] = 10
        # lista.set(5, 9)
        ponteiro = self._pega_no(index)
        if ponteiro:
            ponteiro.dado.dado = elem
        else:
            raise IndexError("list index out of range")
    

    def index(self, elem):
        """
        retorna o indice do elemento na lista
        """
        ponteiro = self.inicio
        i = 0
        while(ponteiro):
            if ponteiro.dado == elem:
                return i
            ponteiro = ponteiro.prox
            i = i + 1
        raise ValueError("{} is not in list".format(elem))
    
    def insere(self, index, elem):
        """
        Insere elemento na posicao passada por parametro    
        """
        if index == 0:
            no = No(elem)
            no.prox = self.inicio
            self.inicio = no
        else:
            ponteiro = self._pega_no(index - 1)
            no = No(elem)
            no.prox = ponteiro.prox
            ponteiro.prox = no
        self._size = self._size + 1
    
    def remove(self, elem):
        """
        Remove um elemento da lista
        """
        if self.inicio == None:
            raise ValueError("{} nao esta na lista".format(elem))
        elif self.inicio.dado == elem:
            self.inicio = self.inicio.prox
            self._size = self._size - 1
            return True
        else:
            ancestor = self.inicio
            ponteiro = self.inicio.prox
            while ponteiro:
                if ponteiro.dado == elem:
                    ancestor.prox = ponteiro.prox
                    ponteiro.prox = None
                ancestor = ponteiro
                ponteiro = ponteiro.prox
            self._size = self._size - 1
            return True
        raise ValueError("{} nao esta na lista".format(elem))

    def insere_n_nos(self, num_nos):
        """
        Insere n nos, dado o numero de nos a serem inseridos
        """
        for i in range(num_nos):
            index = random.randint(1, 11 ** 4)
            elem = random.randint(1, 11 ** 4)
            self.insere(index, elem)

    def remove_n_nos(self, num_nos):
        """
        remove n nos, dado o numero de nos a serem removidos
        """
        for i in range(num_nos):
            elem = random.randint(1, 11 ** 4)
            self.remove(elem)

    def __repr__(self):
        r = ""
        ponteiro = self.inicio
        while(ponteiro):
            r = r + str(ponteiro.dado) + "->"
            ponteiro = ponteiro.prox
        return r

    def __str__(self):
        return self.__repr__()