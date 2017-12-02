"""Tests for Trie tree."""

import pytest
from trie import Trie
from trie import Node


@pytest.fixture
def empty():
    """Sample Trie without nodes for testing."""
    return Trie()


@pytest.fixture
def filled():
    """Sample Trie with contents for testing."""
    t = Trie()
    t.insert('hello')
    t.insert('goodbye')
    t.insert('helsinki')
    t.insert('goodlord')
    t.insert('squish')
    t.insert('heckingoodboye')
    return t


def test_created_node_has_attributes():
    """Test attributes of Node."""
    n = Node()
    assert n.letter is None
    assert n.children == {}


def test_trie_has_correct_attributes(empty):
    """Test that Trie has correct attributes on init."""
    assert empty.root.letter == '*'
    assert isinstance(empty.root, Node)


def test_insert_adds_word_to_trie(empty):
    """Test basic insert method on single word."""
    empty.insert('abc')
    assert 'a' in empty.root.children
    assert 'b' in empty.root.children['a'].children
    assert 'c' in empty.root.children['a'].children['b'].children
    assert '$' in empty.root.children['a'].children['b'].children['c'].children


def test_word_ends_after_bling_sign(empty):
    """Test that nothing comes after the '$' sign inserted."""
    empty.insert('a')
    assert 'a' in empty.root.children
    assert '$' in empty.root.children['a'].children
    assert empty.root.children['a'].children['$'].children == {}


def test_word_is_not_added_twice(empty):
    """Test that the same word cannot be added twice."""
    empty.insert('yo')
    a = empty.root.children
    empty.insert('yo')
    b = empty.root.children
    assert a == b
