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

# chr(index + ord('a'))
# order is preorder

    def _print_trie(self, node, word=''):
        if node.is_end_of_word:
            print(word) # print word when it is marked as the end
        
        for i in range(26):
            if node.children[i] is not None:
                new_letter = chr(i + ord('a'))
                self._print_trie(node.children[i],word + new_letter) # gives correct order, can put new_letter + word to flip the word in the other order

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
trie.display()