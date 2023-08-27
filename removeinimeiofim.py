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
    
    def removeFromStart(self):
        if self.head is None:
            return
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        self.length -= 1
    
    def removeFromMiddle(self, pos):
        if pos < 0 or pos >= self.length:
            return
        if pos == 0:
            self.removeFromStart()
        elif pos == self.length - 1:
            self.removeFromEnd()
        else:
            curr = self.head
            for _ in range(pos):
                curr = curr.next
            curr.prev.next = curr.next
            curr.next.prev = curr.prev
            self.length -= 1
    
    def removeFromEnd(self):
        if self.tail is None:
            return
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self.length -= 1
    
    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

doublyLL = DoublyLL()
doublyLL.insertAtEnd(5)
doublyLL.insertini(4)
doublyLL.insertini(3)
doublyLL.insertini(40)
doublyLL.insertini(2)
doublyLL.insertini(1)
doublyLL.insertini(15)
doublyLL.insertAtEnd(30)
doublyLL.removeFromEnd() 
doublyLL.removeFromMiddle(3)
doublyLL.removeFromStart() # Remove o nó do meio (posição 1)
doublyLL.print_list()

        