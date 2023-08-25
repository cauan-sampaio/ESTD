class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertBeginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def printList(self, node):
        if node is None:
            return
        print(node.data)
        self.printList(node.next)

# Create a linked list instance
linked_list = LinkedList()

# Insert elements at the beginning of the linked list
linked_list.insertBeginning(80)
linked_list.insertBeginning(7)
linked_list.insertBeginning(5)
linked_list.insertBeginning(3)


# Print the linked list
linked_list.printList(linked_list.head)
