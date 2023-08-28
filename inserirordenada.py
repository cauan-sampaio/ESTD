class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_sorted_recursive(self, head, data):
        if head is None or data < head.data:
            new_node = Node(data)
            new_node.next = head
            return new_node

        head.next = self.insert_sorted_recursive(head.next, data)
        return head

    def print_list(self, head):
        current = head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

linked_list = LinkedList()

linked_list.head = linked_list.insert_sorted_recursive(linked_list.head, 3)
linked_list.head = linked_list.insert_sorted_recursive(linked_list.head, 1)
linked_list.head = linked_list.insert_sorted_recursive(linked_list.head, 2)
linked_list.head = linked_list.insert_sorted_recursive(linked_list.head, 5)
linked_list.head = linked_list.insert_sorted_recursive(linked_list.head, 4)

linked_list.print_list(linked_list.head)
