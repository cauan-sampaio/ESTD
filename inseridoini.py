class Node():
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class DoublyLL():
    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None
    
    def insertini(self, data):
        newNode = Node(data, None, None)
        if self.head is None:
            self.head = self.tail = newNode
        else:
            newNode.prev = None
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
        self.length += 1
    
    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

doublyLL = DoublyLL()
doublyLL.insertini(1)
doublyLL.insertini(2)
doublyLL.insertini(3)
doublyLL.insertini(4)
doublyLL.print_list()
