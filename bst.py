"""Implementation of a binary search tree data structure."""


class Node(object):
    """Define the Node-class object."""

    def __init__(self, value, left=None, right=None):
        """Constructor for the Node class."""
        self.val = value
        self.left = left
        self.right = right
        self.depth = 0


class BST(object):
    """Define the BST-class object."""

    def __init__(self, starting_values=None):
        """Constructor for the BST class."""
        self.tree_size = 0
        self.left_depth = 0
        self.right_depth = 0

        if starting_values is None:
            self.root = None

        elif isinstance(starting_values, (list, str, tuple, set)):
            self.root.val = starting_values[0]
            self.tree_size += 1
            for i in len(starting_values) - 1:
                self.insert(starting_values[i + 1])

        else:
            raise TypeError('Only iterables or None\
                are valid parameters!')
    