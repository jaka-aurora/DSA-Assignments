# Lesson Exercises

## 07-01: Trie Tree

A trie tree is used for efficient string storage and retrieval.

In this assignment we have implemented `Trie` (prefix tree) data structure. 
There is also `insert` function that add a word into the `Trie`.

* initialize an array of 26 elements 
* it has an empty slots reserved for letters _a-z_ (no other letters supported)


Test the Trie by creating a `display()` method to show/print all the words in the Trie.

* it will also recursively calls `_print_trie()` to handle all child nodes

```python
class TrieNode:
    def __init__(self):
        # Initialize an array of 26 elements to None (for each letter a-z)
        self.children = [None] * 26
        self.is_end_of_word = False  # Flag to mark the end of a word


class Trie:
    def __init__(self):

        self.root = TrieNode()

    def _char_to_index(self, ch):
        return ord(ch) - ord('a')

    def insert(self, word: str):
        current_node = self.root

        for char in word:
            index = self._char_to_index(char)

            # If the corresponding node does not exist, create a new TrieNode
            if current_node.children[index] is None:
                current_node.children[index] = TrieNode()

            # Move to the next node
            current_node = current_node.children[index]

        # After inserting all characters, mark the current node as the end of the word
        current_node.is_end_of_word = True

    def _print_trie(self, node, word=''):
        # TODO: stop/return if end of the word?
        # TODO: Iterate 26 characters and recursively show the child nodes

    def display(self):
        self._print_trie(self.root)

        
        
trie = Trie()
trie.insert("hello")
trie.insert("help")
trie.insert("trie")
trie.insert("tree")
# Plus other words
# trie.display()
```



## 07-02: TrieNode with characters

* Now in **07-01** solution shows only indexes _0-26_ as a child nodes.
* Try to add character (with `char` property) to `TrieNode` and to show that info when you debug Nodes.  

Recursive call in `_print_trie()` should be also change like this:

```
self._print_trie(node.children[i], word + node.children[i].char)
```

## 07-03: Trie Tree with Scandinavian characters

Implement support to Trie tree to Scandinavian characters _'å', 'ä'_ and _'ö'_.

Extra:
* You can use a `dictionary (dict)` instead of a fixed-size array for children to handle any characters added.