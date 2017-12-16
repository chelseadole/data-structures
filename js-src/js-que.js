'use strict';

const DLL = require('./js-doubly-linked-list')

class Queue {
    constructor(){
        this.dll = new DLL()
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

    peek() {
        if (this.dll.counter === 0) {
            return 'Queue has no values.'
        }
        return this.dll.tail.data;
    }

    size() {
        return this.dll.counter;
    }
}

module.exports = Queue