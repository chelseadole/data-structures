"use strict";

class Node {
    constructor(data, nextNode=None, prevNode=None) {
        this.data = data;
        this.nextNode = nextNode;
        this.prevNode = prevNode
    }
}

class DLL {
    constructor(iter=null) {
        this.head = null;
        this.tail = null;
        if (Array.isArray(iter)) {
            iterable.forEach(item => this.push(item));
        }
        else if (iter != null) {
            throw 'LinkedList only takes arrays as inputs.';
        }
    }

    push(val) {
        this.head = new Node(this.val, this.head);
        this.counter ++;
        if (this.size() == 1) {
            this.tail = this.head;
        }
    }

    pop() {
        if (this.size() == 0) {
            throw 'Cannot pop() from empty DoublyLinkedList.';
        }
        this.counter --;
        var output = self.head.data;
        this.head = self.head.nextNode;
        this.head.prevNode = null;
        return output;
    }

    size() {
        return this.counter;
    }

    search(val) {
        curr = this.head;
        while (curr.data != val) {
            if (curr.nextNode == null) {
                throw 'This value is not in the LinkedList.'
            }
            curr = curr.nextNode;
        }
        return curr;
    }

    remove(val) {
        curr = this.head;
        while (curr.data != val) {
            if (curr.nextNode == null) {
                throw 'Values not in the LinkedList cannot be removed.'
            }
            curr = curr.nextNode;
        }
        if (curr.prevNode) {
            curr.prevNode.nextNode = curr.nextNode;
        }
        if (curr.nextNode) {
            curr.nextNode.prevNode = curr.prevNode;
        }

    }
}