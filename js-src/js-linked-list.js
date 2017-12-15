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

    push(val) {
        this.head = new Node(val, this.head);
        this.counter ++;
    }   

    pop() {
        if (this.size() == 0) {
            throw 'Cannot pop() from empty LinkedList.';
        }
        this.counter --;
        var output = self.head.data;
        this.head = self.head.nextNode;
        return output;
    }
}