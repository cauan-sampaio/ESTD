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

    def delete_middle(self):
        if self.length == 0:
            return
        middle_index = self.length // 2
        self._delete_middle_recursive(self.head, middle_index)
        self.length -= 1

    def _delete_middle_recursive(self, node, target_index, current_index=0):
        if node is None:
            return current_index
        if current_index == target_index - 1:
            node.next = node.next.next
        return self._delete_middle_recursive(node.next, target_index, current_index + 1)

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

my_linked_list.delete_middle()

my_linked_list.display()  # Saída: 1 -> 2 -> 4 -> None
