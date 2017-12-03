"""Trie tree structure."""


class Node(object):
    """Node class."""

    def __init__(self, letter=None, parent=None, end=False):
        """Initialization of Trie node attributes."""
        self.letter = letter
        self.children = {}
        self.parent = parent
        self.end = end

    def __iter__(self):
        """Make children iterable."""
        return self.children.itervalues()


class Trie(object):
    """Trie class."""

    def __init__(self):
        """Initialization of Trie tree."""
        self.root = Node('*')
        self.size = 0

    def insert(self, word):
        """Insert a new word into the tree."""
        current = self.root
        if self.contains(word) or type(word) is not str:
            return
        for letter in word:
            current.children.setdefault(letter, Node(letter, current))
            current = current.children[letter]
        current.end = True
        self.size += 1
        return

    def contains(self, word):
        """Check if Trie contains word."""
        current = self.root
        for letter in word:
            if letter not in current.children:
                return False
            current = current.children[letter]
        if current.end:
            return True
        return False

    def size(self):
        """Return number of words in Trie tree."""
        return self.size

    def remove(self, word):
        """Remove word from trie."""
        # if not self.contains(word):
        #     raise KeyError('This word is not in the Trie.')
        # current = self.root
        # for letter in word:
        current = self.root
        for letter in range(len(word - 1)):
            if letter not in current.children:
                raise TypeError('This word is not in Trie.')
            current = current.children[letter]
        current = current.parent
        while len(current.children) == 1:
            current.children.clear()
            current = current.parent
