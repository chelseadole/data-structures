"""Trie tree structure."""


class Node(object):
    """Node class."""

    def __init__(self, letter=None):
        """Initialization of Trie node attributes."""
        self.letter = letter
        self.children = {}


