class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0  # Initialize the length attribute

    def insertend(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = newNode
        self.length += 1  # Increment the length

    def printList(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next

# Create a linked list instance
linked_list = LinkedList()

# Insert elements at the end of the linked list
linked_list.insertend(5)
linked_list.insertend(23)
linked_list.insertend(10)
linked_list.insertend(1)
linked_list.insertend(7)


# Print the linked list
linked_list.printList()

