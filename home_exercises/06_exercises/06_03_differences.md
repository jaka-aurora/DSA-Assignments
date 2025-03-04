* Question: Describe differences between one-way and two-way linked list?

One-way linked list:
- each node in the list contains a value and references the next node in the list
- the list can only be read in one direction
- Insreting and deleting nodes is simple, but only if the list is small since we need to go through the list in order to find the previous node 
- Each node stores only one reference so the list technically uses less memory and can be used in cases where that is important

Two-way linked list: 
- each node in this list has a value, a reference to the next node and a reference to the previous node
- because of that the list can be read in both directions
- Inserting and deleting can be more efficient since node's previous reference is readily available
- Because there are two references stored in a node, it uses more memory
- in that sense it is suitable in cases where memory is not a concern but it is more important to be able to move in two directions in a list