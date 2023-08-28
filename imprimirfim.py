class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def imprimirfim(self, head):
        if head == None:
            return
        
        self.imprimirfim(head.next)
        print(head.data)
    
    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

linked_list = LinkedList()
linked_list.head = linked_list.imprimirfim(linked_list.head,1)
linked_list.head = linked_list.imprimirfim(linked_list.head,2)
linked_list.head = linked_list.imprimirfim(linked_list.head,3)
linked_list.head = linked_list.imprimirfim(linked_list.head,4)

linked_list.print_list(linked_list.head)




