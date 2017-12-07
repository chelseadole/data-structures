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
        self.tree_size = 0

    def insert(self, word):
        """Insert a new word into the tree."""
        current = self.root
        if self.contains(word) or type(word) is not str:
            return
        for letter in word:
            current.children.setdefault(letter, Node(letter, current))
            current = current.children[letter]
        current.end = True
        self.tree_size += 1
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
        return self.tree_size

    def remove(self, word):
        """Remove word from trie."""
        current = self.root
        for letter in word:
            if letter not in current.children:
                raise TypeError('This word is not in Trie.')
            current = current.children[letter]
        current = current.parent
        while len(current.children) == 1:
            current.children.clear()
            if current.parent:
                current = current.parent
        self.tree_size -= 1

    def trie_traversal(self, start=None):
        """Depth-first traveral of Trie."""
        self.visited = []

        if start:
            curr = self.root
            for char in start:
                if char in curr.children:
                    curr = curr.children[char]
                return 'Invalid starting string.'
            return self._combo_gen(curr)
        else:
            return self._combo_gen(self.root)

    def _combo_gen(self, start):
        """."""
        for child, child_node in start.children.items():
            import pdb; pdb.set_trace()
            self.visited.append(child)
            for node in child_node.children:
                self.visited.append(child_node.children[node].letter)
                if child_node.children[node].end and not child_node.children:
                    continue
                child_node.children = child_node.children[node].children
        for let in self.visited:
            yield let

    def _trie_gen(self, start):
        """Generator for traversal function."""
        for child in start.children:
            return self._recursive_depth(start.children[child])

    def _recursive_depth(self, node):
        """Recursive helper fn for generator."""
        self.visited.append(node.letter)
        for child in node.children:
            if child.end:
                break
            yield self._recursive_depth(node.children[child])
