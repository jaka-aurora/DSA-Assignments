class DoublyNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = DoublyNode(value)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        new_node.prev = current

    def remove_node(self, value):
        if not self.head:
            return
        
        current = self.head
        
        # If the node to be removed is the head
        if current.value == value:
            self.head = current.next
            if self.head:
                self.head.prev = None
            return
        
        while current and current.value != value:
            current = current.next
        
        # If the node was found, remove it
        if current:
            if current.next:
                current.next.prev = current.prev
            if current.prev:
                current.prev.next = current.next

    def display(self):
        node_list = []
        if not self.head:
            print("List is empty")
            return
        current = self.head
        while current:
            node_list.append(str(current.value))
            if current.next:
                node_list.append(" <-> ")
            current = current.next
        print("".join(node_list))

# Test the implementation
doubly_linked_list = DoublyLinkedList()
doubly_linked_list.append(1)
doubly_linked_list.append(2)
doubly_linked_list.append(3)
doubly_linked_list.remove_node(2)  # Test removing a node
doubly_linked_list.display()  # Expected output: 1 <-> 3