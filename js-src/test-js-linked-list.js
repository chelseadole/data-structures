'use strict';

var linkedList = require('js-linked-list');
var chai = require('chai');
var expect = chai.expect;

describe('linked_list.js tests', () => {
    it('creating a new empty LinkedList', () => {
        let testList = new linkedList.LL();
        expect(testList.size()).to.equal(0);
        expect(testList.head.data).to.equal(null);
        expect(testList.tail.data).to.equal(null);
    });

    it('passing iterable into new LinkedList and pushing.', () => {
        let testList = new linkedList.LL([100, 200, 300, 400, 500]);
        expect(testList.size()).to.equal(5);
        expect(testList.head.data).to.equal(500);
        expect(testList.tail.data).to.equal(100);

    });
