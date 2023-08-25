class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0  
        
    def deletebeginning(self):
        if self.length != 0:
            self.head = self.head.next
            self.length -=1
        else:
            raise Exception("Cannot delete from an empty list")     
my_linked_list = LinkedList()
my_linked_list.append(1)
my_linked_list.append(2)
my_linked_list.append(3)

my_linked_list.delete_beginning()
