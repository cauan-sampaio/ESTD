class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0  

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.length += 1

    def delete_end(self):
        if self.length == 0:
            return
        self._delete_end_recursive(self.head)
        self.length -= 1

    def _delete_end_recursive(self, node):
        if node.next is None or node.next.next is None:
            node.next = None
            return
        self._delete_end_recursive(node.next)

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Exemplo de uso
my_linked_list = LinkedList()
my_linked_list.append(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)

my_linked_list.display()  # Saída: 1 -> 2 -> 3 -> 4 -> None

my_linked_list.delete_end()

my_linked_list.display()  # Saída: 1 -> 2 -> 3 -> None
