#!/usr/bin/python3
'''
Module to create a single linked list in python
'''


class Node():
    '''Class to create a node'''
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        ''' get the data'''
        try:
            return self.__data
        except TypeError as error:
            print(error)

    @data.setter
    def data(self, value):
        if type(value) != int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        '''crate new node'''
        try:
            return self.__next_node
        except BaseException as error:
            print(error)

    @next_node.setter
    def next_node(self, value):
        if value is None or isinstance(value, Node):
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList():
    '''
    clas to sort linked list and print
    '''
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        '''sorted insert new node'''
        new_node = Node(value)
        aux = self.__head
        if aux is None:  # if head is empty
            self.__head = new_node
        elif aux.data > value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current = self.__head
            while True:
                if current.next_node is None:
                    current.next_node = new_node
                    break
                elif current.next_node.data >= value:
                    new_node.next_node = current.next_node
                    current.next_node = new_node
                    break
                current = current.next_node

    def __str__(self):
        '''print string representation of linked list'''
        str_node = ""
        data_node = self.__head
        while data_node is not None:
            if data_node.next_node is None:
                str_node += str(data_node.data)
            else:
                str_node += str(data_node.data)+"\n"
            data_node = data_node.next_node
        return str_node
