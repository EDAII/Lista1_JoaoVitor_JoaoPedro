# Python implementation of Doubly linked list 
import sys
import random
import time

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None 
        self.tail = None

    # Insert 'value' at the front of the list
    def insert_at_front(self, value):
        node = Node(value)
        if self.is_empty():
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
     
    #  insert value at the back of the linked list
    def insert_at_back(self, value):
        node = Node(value)
        if self.is_empty():
            self.head = node
        else:
           self.tail.next = node
           node.prev = self.tail
           self.tail = node
    
    # inserts value after key
    def insert_after(self, key, value):
        node = Node(value)

        # find the position of key
        curr = self.head
        while curr != None and curr.data != key:
            curr = curr.next

        if curr == None:
            raise ValueError('Chave não achada')

        if curr.next == None:
            curr.next = node
            node.prev = curr
            self.tail = node 
        else:
            next_node = curr.next
            curr.next = node
            node.prev = curr
            node.next = next_node
            next_node.prev = node

    # returns the data at first node 
    def top_front(self):
        if self.is_empty():
            print('List is empty')
            return

        return self.head.data

    # returns the data at last node 
    def top_back(self): 
        if self.is_empty():
            print('List is empty')
            return

        curr = self.head
        while curr.next != None:
            curr = curr.next

        return curr.data

    # removes the item at front of the linked list and return 
    def pop_front(self):
        if self.is_empty():
            print('List is empty')
            return

        next_node = self.head.next
        if (next_node != None):
            next_node.prev = None
        item = self.head.data
        self.head = next_node
        return item

    # remove the item at the end of the list and return 
    def pop_back(self):
        if self.is_empty():
            print('List is empty')
            return

        item = self.tail.data
        prev = self.tail.prev

        if prev != None:
            prev.next = None

        self.tail.prev = None
        self.tail = prev

        return item

    # removes an item with value 'key'
    def remove(self, key):
        if self.is_empty():
            print('List is empty')
            return

        # find the position of the key
        curr = self.head

        while curr != None and curr.data != key:
            curr = curr.next

        if curr == None:
            raise ValueError('Chave não achada')

        # if curr is head, delete the head
        if curr.prev == None:
            self.pop_front()
        elif curr.next == None: # if curr is last item
            self.pop_back()
        else: #anywhere between first and last node
            next_node = curr.next
            prev_node = curr.prev

            prev_node.next = next_node
            next_node.prev = prev_node

            curr.next = None 
            curr.prev = None
            curr = None

    # check if the key is in the list
    def find(self, key):
        if self.is_empty():
            print('List is empty')
            return False

        curr = self.head
        while curr != None and curr.data != key:
            curr = curr.next

        if curr == None:
            return False

        return True

    # check if the list is empty
    def is_empty(self):
        return self.head == None

    # print all the items
    def printlist(self):
        if self.is_empty():
            print("Nothing to display")
        else:
            curr = self.head
            while (curr != None):
                sys.stdout.write(str(curr.data) + ' ')
                curr = curr.next

            print('')
    
    def print_reverse(self):
        if self.is_empty():
            print("Nothing to display")
        else:
            curr = self.tail
            while (curr != None):
                sys.stdout.write(str(curr.data) + ' ')
                curr = curr.prev
    
            print('')
	
    def insert_n_nodes(self, index, elem, num_nodes):
        for i in range(num_nodes):
            self.insert_after(index, elem)

    def remove_n_nodes(self, elem, num_nodes):
        for i in range(num_nodes):
            self.remove(elem)

# def main():
# 	lista = DoublyLinkedList()
# 	for i in range(10 ** 4):
# 		lista.insert_at_front(random.randint(1, 11 ** 4))   
# 	for i in range(0,20):
# 		operation = random.randint(1,10)        
# 		if 1 <= operation <= 8:
# 			try:
# 				print('#'*100)
# 				print('Realiza busca sequencial')
# 				elem = random.randint(1, 11 ** 4)
# 				# print('Tamanho lista:',len(lista))
# 				print('Elemento procurado:',elem)
# 				start = time.time()
# 				lista.find(elem)
# 				end = time.time()
# 				elapsed_time = end - start
# 				print('Tempo para realizar busca sequencial:', elapsed_time)
# 			except ValueError:
# 				print("Valor não encontrado")
# 		elif operation == 9:
# 			print('#'*100)
# 			print('Insere elementos da lista')
# 			try:
# 				lista.insert_n_nodes(random.randint(1, 10 ** 4), random.randint(1, 11 ** 4), 10 ** 3)
# 			except:
# 				print("Chave não achada")
				
# 		elif operation == 10:
# 			print('#'*100)
# 			print('Removendo elementos da lista')
# 			try:
# 				lista.remove_n_nodes(random.randint(1, 9 ** 3), 10 ** 3)				
# 			except ValueError:
# 				print("Chave não achada")

# main()