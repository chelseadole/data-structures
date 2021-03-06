"""Tests for the Binary Search Tree."""

import pytest
from bst import BST
from bst import Node


@pytest.fixture
def sample_bst():
    """Make a sample_bst for testing."""
    from bst import BST
    return BST()


def test_bst_exists(sample_bst):
    """Test that the BST class makes something."""
    assert sample_bst


def test_bst_can_take_list_at_initialization():
    """Test that the BST can take a list."""
    from bst import BST
    b = BST([1, 2, 3])
    assert b.size() == 3
    assert b.depth() == 2
    assert b.left_depth == 0
    assert b.right_depth == 2


def test_bst_can_take_tuple_at_initialization():
    """Test that the BST can take a tuple."""
    from bst import BST
    b = BST((1, 2, 3))
    assert b.size() == 3
    assert b.depth() == 2
    assert b.left_depth == 0
    assert b.right_depth == 2


def test_bst_can_take_string_at_initialization():
    """Test that the BST can take a string."""
    from bst import BST
    b = BST('abc')
    assert b.size() == 3
    assert b.depth() == 2
    assert b.left_depth == 0
    assert b.right_depth == 2


def test_insert_increases_depth(sample_bst):
    """Test that the insert method increases the output of the depth method."""
    assert sample_bst.depth() == 0
    sample_bst.insert(1)
    assert sample_bst.depth() == 0
    sample_bst.insert(2)
    assert sample_bst.depth() == 1


def test_insert_increases_size(sample_bst):
    """Test that the insert method increases the output of the size method."""
    assert sample_bst.size() == 0
    sample_bst.insert(1)
    assert sample_bst.size() == 1
    sample_bst.insert(2)
    assert sample_bst.size() == 2


def test_insert_increases_tree_size(sample_bst):
    """Test that the insert method increases the tree_size attribute."""
    assert sample_bst.tree_size == 0
    sample_bst.insert(1)
    assert sample_bst.tree_size == 1
    sample_bst.insert(2)
    assert sample_bst.tree_size == 2


def test_search_right(sample_bst):
    """Assert that the search method returns something and that it's a Node."""
    from bst import Node
    sample_bst.insert(1)
    sample_bst.insert(2)
    sample_bst.insert(3)
    found = sample_bst.search(3)
    assert found.val == 3
    assert isinstance(found, Node)


def test_search_left(sample_bst):
    """Assert that the search method returns something and that it's a Node."""
    from bst import Node
    sample_bst.insert(3)
    sample_bst.insert(2)
    sample_bst.insert(1)
    found = sample_bst.search(3)
    assert found.val == 3
    assert isinstance(found, Node)


def test_search_not_found_returns_none(sample_bst):
    """Assert that the search method returns None when value isn't found."""
    sample_bst.insert(1)
    sample_bst.insert(2)
    sample_bst.insert(3)
    found = sample_bst.search(4)
    assert found is None


def test_contains_right(sample_bst):
    """Assert that the contains method returns True."""
    sample_bst.insert(1)
    sample_bst.insert(2)
    sample_bst.insert(3)
    found = sample_bst.contains(3)
    assert found is True


def test_contains_left(sample_bst):
    """Assert that the contains method returns True."""
    sample_bst.insert(3)
    sample_bst.insert(2)
    sample_bst.insert(1)
    found = sample_bst.contains(3)
    assert found is True


def test_contains_not_found_returns_none(sample_bst):
    """Assert that the contains method returns False when value isn't found."""
    sample_bst.insert(1)
    sample_bst.insert(2)
    sample_bst.insert(3)
    found = sample_bst.contains(4)
    assert found is False


def test_that_bst_doesnt_work_with_non_iterable():
    """Test that BST only takes iterable inputs."""
    with pytest.raises(TypeError):
        BST({0: 0, 1: 1, 2: 2})


def test_adding_preexisting_node_is_not_added(sample_bst):
    """Test that adding a node val that exists does not increase BST."""
    assert sample_bst.size() == 0
    sample_bst.insert(5)
    sample_bst.insert(5)
    sample_bst.insert(5)
    assert sample_bst.size() == 1


def test_that_negative_numbers_work_with_insert(sample_bst):
    """Test that negative numbers are covered in insert."""
    sample_bst.insert(-500)
    assert sample_bst


def test_node_attributes_exist():
    """Test that node attributes are in Node class."""
    n = Node(1)
    assert n.val == 1
    assert n.left is None
    assert n.right is None
    assert n.depth == 0


def test_node_attribute_depth_changes(sample_bst):
    """Test that node attribute depth increases."""
    sample_bst.insert(4)
    sample_bst.insert(3)
    sample_bst.insert(2.5)
    assert sample_bst.search(4).depth == 0
    assert sample_bst.search(3).depth == 1
    assert sample_bst.search(2.5).depth == 2


def test_node_left_and_right_attributes_change():
    """Test that left and right node attributes are added with insert."""
    b = BST([5])
    b.insert(4)
    b.insert(6)
    assert b.root.left.val == 4
    assert b.root.right.val == 6


def test_root_val_with_no_val_at_initialization(sample_bst):
    """Test that root is None."""
    assert sample_bst.root is None


def test_in_order_indexerrors_with_empty_tree(sample_bst):
    """Test that in_order raises an IndexError if the tree is empty."""
    with pytest.raises(IndexError):
        sample_bst.in_order()


def test_pre_order_indexerrors_with_empty_tree(sample_bst):
    """Test that pre_order raises an IndexError if the tree is empty."""
    with pytest.raises(IndexError):
        sample_bst.pre_order()


def test_post_order_indexerrors_with_empty_tree(sample_bst):
    """Test that post_order raises an IndexError if the tree is empty."""
    with pytest.raises(IndexError):
        sample_bst.post_order()


def test_breadth_first_indexerrors_with_empty_tree(sample_bst):
    """Test that breadth_first raises an IndexError if the tree is empty."""
    with pytest.raises(IndexError):
        sample_bst.breadth_first()


def test_in_order_size_one(sample_bst):
    """Check for the correct output of in_order on a tree of size 1."""
    sample_bst.insert(1)
    gen = sample_bst.in_order()
    assert next(gen) == 1


def test_pre_order_size_one(sample_bst):
    """Check for the correct output of pre_order on a tree of size 1."""
    sample_bst.insert(1)
    gen = sample_bst.pre_order()
    assert next(gen) == 1


def test_post_order_size_one(sample_bst):
    """Check for the correct output of post_order on a tree of size 1."""
    sample_bst.insert(1)
    gen = sample_bst.post_order()
    assert next(gen) == 1


def test_breadth_first_size_one(sample_bst):
    """Check for the correct output of breadth_first on a tree of size 1."""
    sample_bst.insert(1)
    gen = sample_bst.breadth_first()
    assert next(gen) == 1


LEFT_IMBALANCED = [6, 5, 4, 3, 2, 1]
RIGHT_IMBALANCED = [1, 2, 3, 4, 5, 6]
SAMPLE_TREE = [20, 12, 10, 1, 11, 16, 30, 42, 28, 27]


def test_in_order_left_imba():
    """Check for the correct output of iot on a left-imbalanced tree."""
    tree = BST(LEFT_IMBALANCED)
    gen = tree.in_order()
    output = []
    for i in range(6):
        output.append(next(gen))
    assert output == [1, 2, 3, 4, 5, 6]


def test_pre_order_left_imba():
    """Check for the correct output of preo-t on a left-imbalanced tree."""
    tree = BST(LEFT_IMBALANCED)
    gen = tree.pre_order()
    output = []
    for i in range(6):
        output.append(next(gen))
    assert output == [6, 5, 4, 3, 2, 1]


def test_post_order_left_imba():
    """Check for the correct output of posto-t on a left-imbalanced tree."""
    tree = BST(LEFT_IMBALANCED)
    gen = tree.post_order()
    output = []
    for i in range(6):
        output.append(next(gen))
    assert output == [1, 2, 3, 4, 5, 6]


def test_breadth_first_left_imba():
    """Check for the correct output of bft on a left-imbalanced tree."""
    tree = BST(LEFT_IMBALANCED)
    gen = tree.breadth_first()
    output = []
    for i in range(6):
        output.append(next(gen))
    assert output == [6, 5, 4, 3, 2, 1]


def test_in_order_right_imba():
    """Check for the correct output of iot on a right-imbalanced tree."""
    tree = BST(RIGHT_IMBALANCED)
    gen = tree.in_order()
    output = []
    for i in range(6):
        output.append(next(gen))
    assert output == [1, 2, 3, 4, 5, 6]


def test_pre_order_right_imba():
    """Check for the correct output of preo-t on a right-imbalanced tree."""
    tree = BST(RIGHT_IMBALANCED)
    gen = tree.pre_order()
    output = []
    for i in range(6):
        output.append(next(gen))
    assert output == [1, 2, 3, 4, 5, 6]


def test_post_order_right_imba():
    """Check for the correct output of posto-t on a right-imbalanced tree."""
    tree = BST(RIGHT_IMBALANCED)
    gen = tree.post_order()
    output = []
    for i in range(6):
        output.append(next(gen))
    assert output == [6, 5, 4, 3, 2, 1]


def test_breadth_first_right_imba():
    """Check for the correct output of bft on a right-imbalanced tree."""
    tree = BST(RIGHT_IMBALANCED)
    gen = tree.breadth_first()
    output = []
    for i in range(6):
        output.append(next(gen))
    assert output == [1, 2, 3, 4, 5, 6]


def test_in_order_sample_tree():
    """Check for the correct output of iot on a sample tree."""
    tree = BST(SAMPLE_TREE)
    gen = tree.in_order()
    output = []
    for i in range(10):
        output.append(next(gen))
    assert output == [1, 10, 11, 12, 16, 20, 27, 28, 30, 42]


def test_pre_order_sample_tree():
    """Check for the correct output of preo-t on a sample tree."""
    tree = BST(SAMPLE_TREE)
    gen = tree.pre_order()
    output = []
    for i in range(10):
        output.append(next(gen))
    assert output == [20, 12, 10, 1, 11, 16, 30, 28, 27, 42]


def test_post_order_sample_tree():
    """Check for the correct output of posto-t on a sample tree."""
    tree = BST(SAMPLE_TREE)
    gen = tree.post_order()
    output = []
    for i in range(10):
        output.append(next(gen))
    assert output == [1, 11, 10, 16, 12, 27, 28, 42, 30, 20]


def test_breadth_first_sample_tree():
    """Check for the correct output of bft on a right-imbalanced tree."""
    tree = BST(SAMPLE_TREE)
    gen = tree.breadth_first()
    output = []
    for i in range(10):
        output.append(next(gen))
    assert output == [20, 12, 30, 10, 16, 28, 42, 1, 11, 27]
