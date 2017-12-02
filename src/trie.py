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

