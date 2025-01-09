## 06-01. Remove a node from a one-way linked list

In this task, you use a one-way linked list. Implement a function that removes a given node from the list.

In this task there is partly defined a one-way linked list. There is a Node class that contains a value and a reference to the next node.
And also a LinkedList class that manages nodes and provides methods for adding nodes.

* Implement the remove_node(value) method, which searches for a node based on its value and removes it from the list.
* Test also if the node to be removed is the first node or if no node is found.


Example code:

```python
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

    def remove_node(self, value):
        # TODO: Implement node removal logic
        pass

    def display(self):
        # TODO: Implement display logic
        pass

# Test the implementation
linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.remove_node(2)  # Test removing a node
linked_list.display()  # Expected output: 1 -> 3
```

## 06-02. Remove a node from a doubly linked list

In this task, you use a double linked list. Implement a function that removes a given node from the double linked list.

DoublyLinkedList class that manages nodes and provides methods for adding nodes is already partly defined.

* Implement the remove_node(value) method, which searches for a node based on its value and removes it from the list.
* Test also if the node to be removed is the first or last node or if no node is found.

Example code:

python

```python
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
        # Implement node removal logic
        pass

    def display(self):
        # Implement display logic
        pass


# Test the implementation
doubly_linked_list = DoublyLinkedList()
doubly_linked_list.append(1)
doubly_linked_list.append(2)
doubly_linked_list.append(3)
doubly_linked_list.remove_node(2)  # Test removing a node
doubly_linked_list.display()  # Expected output: 1 <-> 3

```

## 06-03. Differences between one-way and double linked list

Question: Describe differences between one-way and two-way linked list?

