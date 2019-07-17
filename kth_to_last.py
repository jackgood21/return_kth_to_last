class node():                   # basic singly linked list implementation
    def __init__(self, data):
        self.data = data
        self.next = None

class linked_list( node ):
    def __init__(self, node):
        self.head = node

    def kth_to_last(self, k): # assuming you cannot pass in an empty list
        length = self.find_length()
        index_to_find = length - 1 - k # take care of indexing starting at 0 by subtracting 1
        return self.find_node(index_to_find)

    def find_length(self):
        length = 1
        node = self.head
        while node.next != None:
            length += 1
            node = node.next
        return length

    def find_node(self, index_to_find): # iterates through list a second time, returning node at index_to_find
        curr_position = 0
        node = self.head
        found = False
        while not found: # do not have to check if null because we know the length
            if curr_position == index_to_find:
                found = True
                return node.data
            else:
                curr_position +=1
                node = node.next
    def print_list(self): # utility print method to check implementation
        node = self.head
        print(node.data)
        while node.next != None:
            print(node.next.data)
            node = node.next

############ TESTING ##############
# linked list looks like 1 -> 2 -> 3 -> 4 -> 5
n1 = node(1)
n2 = node(2)
n3 = node(3)
n4 = node(4)
n5 = node(5)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

the_list = linked_list(n1)
print(the_list.kth_to_last(0)) # expected: 5
print(the_list.kth_to_last(4)) # expected: 1
print(the_list.kth_to_last(2)) # expected: 3
