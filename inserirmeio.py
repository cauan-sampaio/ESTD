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

    def insert_middle(self, data):
        if self.length == 0:
            self.append(data)
            return
        middle_index = self.length // 2
        self._insert_middle_recursive(self.head, data, middle_index)
        self.length += 1

    def _insert_middle_recursive(self, node, data, target_index, current_index=0):
        if node is None:
            return
        if current_index == target_index - 1:
            new_node = Node(data)
            new_node.next = node.next
            node.next = new_node
            return
        self._insert_middle_recursive(node.next, data, target_index, current_index + 1)

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Exemplo de uso
my_linked_list = LinkedList()
my_linked_list.append(1)
my_linked_list.append(3)

my_linked_list.display()  # Saída: 1 -> 3 -> None

my_linked_list.insert_middle(2)

my_linked_list.display()  # Saída: 1 -> 2 -> 3 -> None
