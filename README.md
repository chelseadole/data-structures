# Data-Structures

**Author**: Chelsea Dole

**Coverage**: [![Build Status](https://travis-ci.org/chelseadole/data-structures.svg?branch=master)](https://travis-ci.org/chelseadole/data-structures)

**Resources/Shoutouts**: Nathan Moore (lab partner/amigo)

**Testing Tools**: pytest, pytest-cov

## Sorting Algorithms: 

* **Insertion Sort** - *The insertion sort algorithm sorts a list of numbers by looping through each individual number in the list one by one, and (if they are smaller than the last index) swapping the two numbers. Unlike bubble sort, after this swap the sort continues to swap the number down into lower indexed positions until it finds the right position. The runtime for this function is at worst-case O(n^2), because in that scenario the list would be exactly the reverse of what it should be.*

## Data Structures:

* **Binary Search Tree** — *a BST is a "tree shaped" data structure containing nodes. Each node can have a maximum of two children or "leaves," and all node values are properly located based on its parents and siblings values. Nodes to the left of the "root"/head node have values smaller than the root. Those to the right have values larger than the root. There are no duplicate values.* 

* **Trie Tree** - *a Trie Tree is a "tree shaped" data structure containing nodes with references to letters. These nodes string together (using each node's "children" and "parent" attriutes) to form words. This tree allows for quick lookup time of words, and is used for things such as word suggestion/auto-complete.*

* **Linked List (JavaScript)** - *A singly linked list is a data structure made of nodes, all of which have a single "next" pointer pointing from the head to the tail. The runtime of traversing the LL is O(n) because it grows proportionally with the length of the list.*

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

* insert() = *This Trie insert method adds a word to the trie tree. It first checks to see if the word is already in the tree (in which case it does nothing). Then, it goes through each letter of the word and uses the dictionary function setdefault to add a new letter node if it doesn't already exist, and string together the letters. Finally, it increases the tree's size attribute. The time complexity is O(len(word)), because the length of runtime depends on the size of the word you're inserting.*

* contains() = *This Trie method checks if the tree contains a certain word. It does this by iterating through each letter of the word and checking if the letter node's children dictionary contains a key to the next letter in the word. If at any point it doesnt (or if the last letter of the word doesn't have the "end" attribute as True) it returns False. The time complexity is at worst case, O(n), because in the worst case scenario, you have just one word in the tree, and you have to check through all the letters in that one word.*

* size() = *This Trie method returns the number of words in the tree by returning the tree's size attribute, which is incremented and decremented in insert() and remove() respectively. Time complexity should be O(1), because it just returns a number: the attribute of Trie.*

* remove() = *This Trie method removes a word from the tree. First it traverses to the node of the last letter of the tree (and raises an error if the word doesnt exist). Once at the last letter, it moves backwards, deleting references to the children/letters below. Time complexity should be O(n * 2), because worst case scenario, the word you're removing is the only word in the tree, and you had to traverse all the way down the letters then come back up.*

