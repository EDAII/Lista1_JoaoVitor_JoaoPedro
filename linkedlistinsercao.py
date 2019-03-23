import random
from node  import Node
import time

sequencial = []

class LinkedList:
    def __init__(self):
        self.head = None
        self._size = 0
    
    def append(self, elem):        
        if self.head:
            # inserção quando a lista já possui elementos
            pointer = self.head
            while(pointer.next):
                pointer = pointer.next
            pointer.next = Node(elem)
        else:
            # primeira inserção
            self.head = Node(elem)
        self._size = self._size + 1

    def _getnode(self, index):
        pointer = self.head
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("list index out of range")
        return pointer


    def __len__(self):
        """" Retorna o tamanho da lista"""
        return self._size

    def __getitem__(self, index):        
        # a = lista[i]
        pointer = self._getnode(index)
        if pointer:
            return pointer.data
        raise IndexError("list index out of range")

    def __setitem__(self, index, elem):
        # lista[i] = 10
        # lista.set(5, 9)
        pointer = self._getnode(index)
        if pointer:
            pointer.data.data = elem
        else:
            raise IndexError("list index out of range")
    

    def index(self, elem):
        """ retorna o índice do elemento na lista"""
        pointer = self.head
        i = 0
        while(pointer):
            if pointer.data == elem:
                return i
            pointer = pointer.next
            i = i + 1
        raise ValueError("{} is not in list".format(elem))
    
    def insert(self, index, elem):
        if index == 0:
            node = Node(elem)
            node.next = self.head
            self.head = node
        else:
            pointer = self._getnode(index - 1)
            node = Node(elem)
            node.next = pointer.next
            pointer.next = node
        self._size = self._size + 1
    
    def remove(self, elem):
        if self.head == None:
            raise ValueError("{} is not in list".format(elem))
        elif self.head.data == elem:
            self.head = self.head.next
            self._size = self._size - 1
            return True
        else:
            ancestor = self.head
            pointer = self.head.next
            while pointer:
                if pointer.data == elem:
                    ancestor.next = pointer.next
                    pointer.next = None
                ancestor = pointer
                pointer = pointer.next
            self._size = self._size - 1
            return True
        raise ValueError("{} is not in list".format(elem))

    def insert_n_nodes(self, index, elem, num_nodes):
        for i in range(num_nodes):
            self.insert(index, elem)

    def remove_n_nodes(self, elem, num_nodes):
        for i in range(num_nodes):
            self.remove(elem)

    def __repr__(self):
        r = ""
        pointer = self.head
        while(pointer):
            r = r + str(pointer.data) + "->"
            pointer = pointer.next
        return r

    def __str__(self):
        return self.__repr__()

def main():
    lista = LinkedList()
    for i in range(10 ** 4):
        lista.append(random.randint(1, 11 ** 4))   
    for i in range(0,20):
        operation = random.randint(1,10)        
        if 9 <= operation <= 10:
            try:
                print('#'*100)
                print('Realiza busca sequencial')
                elem = random.randint(1, 11 ** 4)
                print('Tamanho lista:',len(lista))
                print('Elemento procurado:',elem)
                start = time.time()
                lista.index(elem)
                end = time.time()
                elapsed_time = end - start
                print('Tempo para realizar busca sequencial:', elapsed_time)
            except ValueError:
                print("Valor não encontrado")
        elif 1 <= operation <= 4:
            print('#'*100)
            print('Insere elementos da lista')
            lista.insert_n_nodes(random.randint(1, 10 ** 4), random.randint(1, 11 ** 4), 10 ** 3)
        elif 4 <= operation <= 8:
            print('#'*100)
            print('Removendo elementos da lista')            
            lista.remove_n_nodes(random.randint(1, 9 ** 3), 10 ** 3)

main()