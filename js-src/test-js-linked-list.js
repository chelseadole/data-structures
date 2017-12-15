'use strict';

var linkedList = require('js-linked-list');
var chai = require('chai');
var expect = chai.expect;

describe('linked_list.js tests', () => {
    it('creating a new empty LinkedList', () => {
        var testList = new linkedList.LL();
        expect(testList.size()).to.equal(0);
        expect(testList.head.data).to.equal(null);
        expect(testList.tail.data).to.equal(null);
    });

    it('passing iterable into new LinkedList and pushing.', () => {
        var testList = new linkedList.LL([100, 200, 300, 400, 500]);
        expect(testList.size()).to.equal(5);
        expect(testList.head.data).to.equal(500);
        expect(testList.tail.data).to.equal(100);

    });
 
    it('testing push method changes head and tail', () => {
        var testList = new linkedList.LL();
        testList.push('yo');
        expect(testList.tail.data).to.equal('yo');
        expect(testList.head.data).to.equal('yo');
    });

    it('test push method adds one to size.', () => {
        var testList = new linkedList.LL();
        testList.push(1);
        expect(testList.size()).to.equal(1);
    });

    it("test pop on non-empty list.", () => {
        var testList = new linkedList.LL();
        testList.push(5);
        testList.push(4);
        testList.push(3);
        expect(testList.head.data).to.equal(3);
        expect(testList.pop()).to.equal(3);
        expect(testList.head.data).to.equal(4);
    });
