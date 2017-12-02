"""Trie tree structure."""


class Node(object):
    """Node class."""

    def __init__(self, letter=None):
        """Initialization of Trie node attributes."""
        self.letter = letter
        self.children = {}


class Trie(object):
    """Trie class."""

    def __init__(self):
        """Initialization of Trie tree."""
        self.root = Node('*')
        self.size = 0

    def insert(self, word):
        """Insert string into Trie."""
        current = self.root
        word = word + '$'
        while word:
            if word[0] == '$':
                return "This word is already in the Trie."
            if word[0] in current.children:
                current = current[word[0]]
            else:
                for i in word:
                    current.children[i] = Node(i)
                    current = current.children[i]
                break
