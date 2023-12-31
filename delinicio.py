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

    def delete_beginning(self):
        if self.length != 0:
            self.head = self._delete_recursive(self.head)
            self.length -= 1
        else:
            raise Exception("Cannot delete from an empty list")

    def _delete_recursive(self, node):
        if node is None:
            return None
        return node.next

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

my_linked_list.display()  # Saída: 1 -> 2 -> 3 -> None

my_linked_list.delete_beginning()
my_linked_list.display()  # Saída: 2 -> 3 -> None
