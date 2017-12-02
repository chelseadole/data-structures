"""Trie tree structure."""


class Node(object):
    """Node class."""

    def __init__(self, letter=None):
        """Initialization of Trie node attributes."""
        self.letter = letter
        self.children = {}

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
        current.children['$'] = Node()
        return

    def contains(self, word):
        """Return True if word in trie."""
        current = self.root
        # if len(word) == 1:
        #     import pdb; pdb.set_trace()
        #     if '$' in current.children[word].children:
        #         return True
        while word:
            if word[0] in current.children:
                current = current.children[word[0]]
                word = word[1:]
            else:
                return False
        return True

if __name__ == "__main__":
    t = Trie()
    t.insert('hello')
    t.insert('hellogoodbye')
    t.insert('helsinki')
    print(t.contains('hello'))
    print(t.contains('hellogoodbye'))
    print(t.contains('helsinki'))
    print(t.contains('ballsackery'))
    print(t.contains('hellgo'))
