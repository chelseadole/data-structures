'use strict';

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
      iter.forEach(item => this.push(item));
    }
    else if (iter !== null) {
      throw 'LinkedList only takes arrays as inputs.';
    }
  }

  push(val) {
    this.head = new Node(val, this.head);
    this.counter ++;
  }

  pop() {
    if (this.counter === 0) {
      throw 'Cannot pop() from empty LinkedList.';
    }
    var output = this.head.data;
    this.head = this.head.nextNode;
    this.counter --;
    return output;
  }

  size() {
    return this.counter;
  }

  search(val) {
    var curr = this.head;
    while (curr.data !== val) {
      if (curr.nextNode === null) {
        throw 'This value is not in the LinkedList.';
      }
      curr = curr.nextNode;
    }
    return curr;
  }

  remove(val) {
    var curr = this.head;
    if (this.head.data === val) {
      this.head = this.head.nextNode;
      return val;
    }
    if (this.head === null) {
      throw 'Cannot remove vals from empty LinkedList.';
    }
    while (curr) {
      if (curr.nextNode === null) {
        throw 'Values not in the LinkedList cannot be removed.';
      }
      else if (curr.nextNode.data === val) {
        curr.nextNode = curr.nextNode.nextNode;
        return val;
      }
      curr = curr.nextNode;
    }
  }

  display() {
    var start_paren = '(';
    if (this.head === null) {
      return '()';
    }
    var curr = this.head;
    while (curr) {
      if (curr.nextNode === null) {
        start_paren += curr.data + ')';
        return start_paren;
      }
      else {
        start_paren += curr.data + ', ';
        curr = curr.nextNode;
      }
    }
  }
}

