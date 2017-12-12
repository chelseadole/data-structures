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
    assert n.end is False


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


def test_word_has_end_attribute(empty):
    """Test that nothing comes after the  sign inserted."""
    empty.insert('a')
    assert 'a' in empty.root.children
    assert empty.root.children['a'].end is True


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


def test_insert_adds_multiple_words(filled_2):
    """Test that insert works with multiple words."""
    keys = filled_2.root.children.keys()
    assert 'a' in keys and 'q' in keys
    assert len(keys) == 2
    assert len(filled_2.root.children['a'].children) == 2
    assert 'b' in filled_2.root.children['a'].children
    assert 'z' in filled_2.root.children['a'].children


def test_insert_adds_multiple_words_using_contains(filled_1):
    """Test combo of contains and insert method."""
    assert filled_1.contains('hello')
    assert filled_1.contains('goodbye')
    assert filled_1.contains('helsinki')
    assert filled_1.contains('goodlord')
    assert filled_1.contains('squish')
    assert filled_1.contains('heckingoodboye')
    assert not filled_1.contains('thisisnothere')


def test_contains_where_it_returns_false(filled_2, filled_1):
    """Test false contains."""
    assert not filled_2.contains('nooooope')
    assert not filled_1.contains('h')
    assert not filled_1.contains('good')
    assert not filled_1.contains('squi')


def test_size_method_on_empty_trie(empty):
    """Test size on empy trie instance."""
    assert empty.size() == 0


def test_size_method_on_filled_trie(filled_1):
    """Test size on empy trie instance."""
    assert filled_1.size() == 6


def test_size_method_on_second_filled_trie():
    """Test size on empy trie instance."""
    t = Trie()
    t.insert('abc')
    t.insert('az')
    t.insert('a')
    t.insert('q')
    assert t.size() == 4


def test_remove_method_doesnt_work_without_word(filled_1):
    """Test that the size method will raise TypeError."""
    with pytest.raises(TypeError):
        filled_1.remove('thiswordisnotindict')


def test_deleting_single_word(empty):
    """."""
    empty.insert('ace')
    empty.remove('ace')
    assert empty.size() == 0
    assert empty.contains('ace') is False


def test_remove_will_remove_word_from_dict(filled_1):
    """Test remove method will remove word off Trie."""
    assert filled_1.contains('heckingoodboye')
    filled_1.remove('heckingoodboye')
    assert filled_1.contains('heckingoodboye') is False


def test_remove_wont_remove_words_with_same_beginning(empty):
    """Test that remove method wont remove words if they start with the same letters."""
    empty.insert('antidisestablishmentarianism')
    empty.insert('antimatter')
    empty.remove('antimatter')
    assert empty.contains('antidisestablishmentarianism')
    assert empty.contains('antimatter') is False


def test_size_decreases_with_removing_node(filled_2):
    """Test size of tree reduces with you delete a word."""
    assert filled_2.size() == 4
    filled_2.remove('az')
    assert filled_2.size() == 3


def test_trie_autocomplete_on_filled_tree_letter_h(filled_1):
    """Autocomplete tests on filled tree."""
    a = filled_1.autocomplete('h')
    assert next(a) == 'hello'
    assert next(a) == 'helsinki'
    assert next(a) == 'heckingoodboye'
    with pytest.raises(StopIteration):
        assert next(a)


def test_trie_autocomplete_on_filled_tree_letter_g(filled_1):
    """Autocomplete tests on filled tree."""
    a = filled_1.autocomplete('good')
    assert next(a) == 'goodbye'
    assert next(a) == 'goodlord'


def test_trie_autocomplete_where_no_suggestions(filled_1):
    """Autocomplete with a letter not in Trie tree, makes empty list."""
    a = filled_1.autocomplete('z')
    assert a == []


# def test_trie_autocomplete_where_no_suggestions(filled_1):
#     """Autocomplete with a letter not in Trie tree, makes empty list."""
#     a = filled_1.autocomplete('z')
#     assert a == []
