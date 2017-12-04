# Data-Structures

**Author**: Chelsea Dole

**Resources/Shoutouts**: Nathan Moore (lab partner/amigo)

**Testing Tools**: pytest, pytest-cov

## Data Structures:

* **Binary Search Tree** — *a BST is a "tree shaped" data structure containing nodes. Each node can have a maximum of two children or "leaves," and all node values are properly located based on its parents and siblings values. Nodes to the left of the "root"/head node have values smaller than the root. Those to the right have values larger than the root. There are no duplicate values.* 

## Time Complexities:

* balance() = *This BST function returns the balance (or size difference) between the left and right parts of the tree. Its runtime is O(1), because it always takes the same amount of time to run regardless of tree size, and only performs simple subtraction.*

* size() = *This BST function returns the number of nodes/leaves in a tree. Its runtime is O(1), because runtime never changes regardless of tree size. It only returns the value of tree_size, which is created at BST initialization, and changed during the insertion of nodes.*

* insert() = *This BST function inserts a new node into a tree, and uses a helper function called find_home() to find its correctly sorted place in the tree. This function is, depending on the tree, anywhere between O(logn) and O(n), if it's a relatively balanced tree, every decision will reduce the number of nodes one has to traverse. But if it's a one-sided tree, one may look over every node -- making it O(n).*

* search() = *This BST function is a reference to check_for_equivalence(), which is recursive, and has a runtime of O(n^2), because every time you're re-calling check_for_equivalence, it looks at every node's equivalence.*

* contains() = *This BST function looks at search(), described above, and for the same reasons has runtime of O(n^2).*

* depth() = *This BST function returns the number of "levels" that the tree has, by finding which of the two sides has the greatest depth, and returning that. It has a runtime of O(1), because no matter the size of the tree, it only performs a comparison operation.*

* in_order() = *This BST traversal function traverses the tree and returns a generator that outputs the node values in numerical order. It has a runtime of O(n), not because you visit every node once (you visit them more than once here) but because the work you do/time you take is constant and grows constantly per node addition.*

* pre_order() = *This BST traversal function returns a generator that outputs the node values in order of the furthest left parent, its left child, then its right child. This traveral then backs up to the parent, and repeats until the whole tree has been traversed. Like in_order, it has a runtime of O(n), not because you visit every node once (you visit them more than once here) but because the work you do/time you take is constant and grows constantly per node addition.*

* post_order() = *This BST traversal function returns a generator that outputs the node values in order of the bottom-most left node, the bottom-most right node, and then those nodes' parent. Then it backs up, and repeats this action with the parent as a new child node, until the whole tree has been traversed. Like in_order and pre_order, it has a runtime of O(n), not because you visit every node once (you visit them more than once here) but because the work you do/time you take is constant and grows constantly per node addition.*

* breadth_first() = *This BST traversal returns a generator that outputs the node values in order of their "levels". It produces first the root, then all nodes (left to right) in the first depth level, then all nodes (left to right) in the second depth level, et cetera. Like in_order, pre_order, and post_order, it has a runtime of O(n), not because you visit every node once (you visit them more than once here) but because the work you do/time you take is constant and grows constantly per node addition.*

* delete() = *This BST method deletes a node if it exists, and returns None if it does not exist. It also rebalances the BST (using the internal _rebalance() method, and resets variables for tree_size. Its time complexity is O(n), because worst case scenario the node to delete is at the very end of a imbalanced tree, and therefore it must go through every node.*



