"use strict";

class Node {
    constructor(data, nextNode=null, prevNode=null) {
        this.data = data
        this.nextNode = nextNode
        this.prevNode = prevNode
    }
}

class DLL {
    constructor(iter=null) {
        this.head = null
        this.tail = null
        this.counter = 0
        if (Array.isArray(iter)) {
            iter.forEach(item => this.push(item))
        }
        else if (iter !== null) {
            return 'LinkedList only takes arrays as inputs.'
        }
    }

    push(val) {
        this.head = new Node(val, this.head)
        this.counter ++
        if (this.size() === 1) {
            this.tail = this.head
        } else {
            this.head.nextNode.prevNode = this.head
        }
    }

    pop() {
        if (this.size() === 0) {
            return 'Cannot pop() from empty DoublyLinkedList.'
        }
        this.counter --
        var output = this.head.data
        this.head = this.head.nextNode
        if (this.head) {
            this.head.prevNode = null
        }
        return output
    }

    size() {
        return this.counter
    }

    search(val) {
        var curr = this.head
        while (curr.data !== val) {
            if (curr.nextNode === null) {
                return 'This value is not in the LinkedList.'
            }
            curr = curr.nextNode
        }
        return curr
    }

    remove(val) {
        var curr = this.head
        var prev = null
        while (curr) {
            if (curr.data == val) {
                this.counter --
                if (curr == this.head) {
                    if (this.head == this.tail) {
                        this.head = null
                        this.tail = null
                        return curr.data
                    }
                    this.head = curr.nextNode
                    this.head.prevNode = null
                    return curr.data
                }
                prev.nextNode = curr.nextNode
                curr.nextNode.prevNode = prev
                return curr.data
            }
            if (curr.nextNode == null) {
                return 'Values not in the DoublyLinkedList cannot be removed.'
            }
            prev = curr
            curr = curr.nextNode
        }
        return curr
    }

    append(val){
        var firstTail = this.tail
        this.tail = new Node(val, this.prevNode=this.tail)
        this.counter ++
        if(firstTail){
            firstTail.nextNode = this.tail
        } else {
            this.head = this.tail
        }
        this.tail.nextNode = null
    }

    shift(){
        if (!this.tail){
            return "Cannot shift() from empty DLL."
        }
        var output = this.tail.data
        this.tail = this.tail.prevNode
        if(this.tail) {
            this.tail.nextNode = null
        } else {
            this.head = null
        }
        this.counter --
        return output
    }


    display() {
        var start_paren = "("
        if (this.head === null) {
            return '()'
        }
        var curr = this.head
        while (curr) {
            if (curr.nextNode === null) {
                start_paren += curr.data + ')'
                return start_paren
            }
            else {
                start_paren += curr.data + ', '
                curr = curr.nextNode
            }
        }
    }
}

module.exports = DLL
