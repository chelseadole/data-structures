"use strict";

class Node {
    constructor(data, nextNode=null) {
        this.data = data;
        this.nextNode = nextNode;
    }
}

class LL {
    constructor(iter=null) {
        this.head = null;
        this.counter = 0;
        if (Array.isArray(iter)) {
            iterable.forEach(item => this.push(item));
        }
        else if (iter != null) {
            throw 'LinkedList only takes arrays as inputs.';
        }
    }
}