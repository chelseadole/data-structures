"""Tests for Trie tree."""

import pytest
from trie import Trie
from trie import Node


@pytest.fixture
def empty():
    """Sample Trie without nodes for testing."""
    return Trie()


@pytest.fixture
def filled_1():
    """Sample Trie with contents for testing."""
    t = Trie()
    t.insert('hello')
    t.insert('goodbye')
    t.insert('helsinki')
    t.insert('goodlord')
    t.insert('squish')
    t.insert('heckingoodboye')
    return t


@pytest.fixture
def filled_2():
    """Sample Trie, with simpler contents."""
    t = Trie()
    t.insert('abc')
    t.insert('az')
    t.insert('a')
    t.insert('q')
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


def test_one_letter_word_works(empty):
    """Test insert method on one letter word."""
    empty.insert('a')
    assert len(empty.root.children) == 1
    assert '$' in empty.root.children['a'].children


# def test_insert_adds_multiple_words(filled_2):
#     """Test that insert works with multiple words."""
#     keys = filled_2.root.children.keys()
#     assert 'a' in keys and 'q' in keys
#     assert len(keys) == 2
#     # assert len(filled_2.root.children['a'].children) == 3
#     assert 'b' in filled_2.root.children['a'].children
#     assert 'z' in filled_2.root.children['a'].children


def test_insert_adds_multiple_words_using_contains(filled_1):
    """Test combo of contains and insert method."""
    assert filled_1.contains('hello')
    assert filled_1.contains('goodbye')
    assert filled_1.contains('helsinki')
    assert filled_1.contains('goodlord')
    assert filled_1.contains('squish')
    assert filled_1.contains('heckingoodboye')
    assert not filled_1.contains('thisisnothere')


def test_size_method_on_empty_trie(empty):
    """Test size on empy trie instance."""
    assert empty.size == 0


def test_size_method_on_filled_trie(filled_1):
    """Test size on empy trie instance."""
    assert filled_1.size == 6


def test_size_method_on_second_filled_trie():
    """Test size on empy trie instance."""
    t = Trie()
    t.insert('abc')
    t.insert('az')
    t.insert('a')
    t.insert('q')
    assert t.size == 4
