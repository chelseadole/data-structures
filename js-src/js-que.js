'use strict';

const DLL = require('./js-doubly-linked-list')

class Q {
    constructor(iter=null){
        this.dll = new DLL()
        if (Array.isArray(iter)) {
            iter.forEach(item => this.enqueue(item))
        }
    }

    enqueue(val) {
        this.dll.push(val)
    }

    dequeue() {
        try {
            return this.dll.shift();
        } catch(e) {
            throw 'Cannot shift() from empty Queue.'
        }
    }

    size() {
        return this.dll.counter;
    }

    peek() {
        if (this.dll.counter === 0) {
            return 'Queue has no values.'
        }
        return this.dll.tail.data;
    }
}

module.exports = Q