class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def remove_node(self, search_value):
        # TODO: Implement node removal logic
        if not self.head:
            return
        current = self.head
        if current.value == search_value: #remove 1st node
            self.head = current.next
            return
        while current.next is not None: # remove any other node
            if current.next.value == search_value:
                current.next = current.next.next
                return
            current = current.next
        pass

    def display(self):
        node_list = []
        if not self.head:
            print("List is empty")
            return
        current = self.head
        node_list.append(str(current.value) + " -> ")
        while current.next is not None:
            current = current.next
            if current.next:
                node_list.append(str(current.value))
            else:
                node_list.append(str(current.value))
        print("".join(node_list))

# Test the implementation
linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
#linked_list.remove_node(1)
linked_list.remove_node(2)
#linked_list.remove_node(3)  # Test removing a node
linked_list.display()  # Expected output: 1 -> 3