"""Trie tree structure."""


class Node(object):
    """Node class."""

    def __init__(self, letter=None, end=False):
        """Initialization of Trie node attributes."""
        self.letter = letter
        self.children = {}
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
        """Insert string into Trie."""
        current = self.root
        if self.contains(word):
            return
        elif len(word) == 1:
            word_node = Node(word)
            current.children[word] = word_node
            current = word_node
        else:
            while word:
                current.children.setdefault(word[0], Node(word[0]))
                current = current.children[word[0]]
                word = word[1:]
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
        if not self.contains(word):
            raise KeyError('This word is not in the Trie.')
