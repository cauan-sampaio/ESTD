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

    def insertAtEnd(self, data):
        if self.head is None:
            self.head = self.tail = Node(data)
        else:
            newNode = Node(data)
            newNode.prev = self.tail
            self.tail.next = newNode
            self.tail = newNode
            self.length += 1

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
    
    def insertAtGivenPosition(self, pos, data):
        if self.head is None or pos == 0:
            self.insertini(data)
        elif pos == self.length:
            self.insertAtEnd(data)
        elif pos < self.length:
            curr = self.head
            count = 0 
            while curr is not None and count < pos:
                curr = curr.next
                count += 1
            newNode = Node(data)
            newNode.next = curr
            newNode.prev = curr.prev
            curr.prev.next = newNode
            curr.prev = newNode
            self.length += 1
    
    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

doublyLL = DoublyLL()
doublyLL.insertAtEnd(4)
doublyLL.insertini(2)
doublyLL.insertAtGivenPosition(1, 3)  
doublyLL.insertini(1)
doublyLL.print_list()

