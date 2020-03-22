# Bring packages to the current workspace
import sys, os
sys.path.append(os.path.abspath(os.path.join('..', 'ds', 'linked_list')))

from list_core import linked_list

class HashTable:
    def __init__(self):
        # Using a dictionary to mapping
        self.hash_table = {}

    def hash_function(self, value, function=1):
        def str_to_ascii(value):
            return ''.join(str(ord(c)) for c in value)

        def get_len(value):
            return len(str(value))

        if function == 1:
            return get_len(value)

        if function == 2:
            return str_to_ascii(value)

    def check_colision(self, hash_of_value):
        if hash_of_value in self.hash_table:
            return True
        return False
    
    def linked_list_generator(self, value, hash_of_value):
        current_value = self.hash_table[hash_of_value]
        if isinstance(current_value, linked_list.LinkedList):
            # append value since the list was already created
            current_value.add_node(value)
            return current_value
        
        new_linked_list = linked_list.LinkedList()
        new_linked_list.add_node(current_value)
        new_linked_list.add_node(value)
        return new_linked_list

    def add_element(self, value):
        hash_of_value = self.hash_function(value)
        # check colision
        if not self.check_colision(hash_of_value):
           self.hash_table[hash_of_value] = value
        # Collision detected, adding a linked list
        else:
            self.hash_table[hash_of_value] = self.linked_list_generator(value, hash_of_value)

    def remove_element(self):
        pass

    def print_hash(self):
        for key in self.hash_table:
            if isinstance(self.hash_table[key], linked_list.LinkedList):
                self.hash_table[key].print_list()
            else:
                print('Value: ', self.hash_table[key])

    def find_element(self):
        pass
        
        
        

        