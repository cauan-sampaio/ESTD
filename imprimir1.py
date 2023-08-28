class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def lista(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    def ntermo(l, n):
        slow_ptr = fast_ptr = l.head
        count = 0
        while count < n and fast_ptr:
            fast_ptr = fast_ptr.next
            count += 1
        while fast_ptr.next != None:
               slow_ptr = slow_ptr.next
               fast_ptr = fast_ptr.next
        return slow_ptr.data if slow_ptr else None

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

my_linked_list = LinkedList()
my_linked_list.lista(1)
my_linked_list.lista(2)
my_linked_list.lista(3)
my_linked_list.lista(4)
my_linked_list.lista(5)
my_linked_list.print_list()
result = my_linked_list.ntermo(2)
print(result)



