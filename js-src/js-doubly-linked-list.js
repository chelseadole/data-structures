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
            this.tail = this.head
        }
    }
}