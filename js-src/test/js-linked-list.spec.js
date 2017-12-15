'use strict';

var linkedList = require('../js-linked-list');
var chai = require('chai');
var expect = chai.expect;

describe('linked_list.js tests', () => {
    it('creating a new empty LinkedList', () => {
        var testList = new linkedList();
        expect(testList.size()).to.equal(0);
        expect(testList.head).to.equal(null);
    });

    it('passing iterable into new LinkedList and pushing.', () => {
        var testList = new linkedList([100, 200, 300, 400, 500]);
        expect(testList.size()).to.equal(5);
        expect(testList.head.data).to.equal(500);

    });
 
    it('testing push method changes head', () => {
        var testList = new linkedList();
        testList.push('yo');
        expect(testList.head.data).to.equal('yo');
    });

    it('test push method adds one to size.', () => {
        var testList = new linkedList();
        testList.push(1);
        expect(testList.size()).to.equal(1);
    });

    it("test pop on non-empty list.", () => {
        var testList = new linkedList();
        testList.push(5);
        testList.push(4);
        testList.push(3);
        expect(testList.head.data).to.equal(3);
        expect(testList.pop()).to.equal(3);
        expect(testList.head.data).to.equal(4);
    });

    it("size function works with push and pop", () => {
        var testList = new linkedList([1, 2, 3, 4, 5]);
        expect(testList.size()).to.equal(5);
        testList.push(0);
        expect(testList.size()).to.equal(6)
        testList.pop();
        expect(testList.size()).to.equal(5);
    });

    it("search on list without searched value", () => {
       var testList = new linkedList();
       testList.push(5);
       expect(testList.search(2)).to.throw('This value is not in the LinkedList.');
    });

    it('correct search method works', () => {
        var testList = new linkedList();
        testList.push(5);
        testList.push(4);
        expect(testList.search(5).data).to.equal(5);
    });

    it("remove method with item in head of list", () => {
        var testList = new linkedList();
        testList.push(1);
        expect(testList.size()).to.equal(1);
        expect(testList.remove(1)).to.equal(1);
        expect(testList.size()).to.equal(0);
    });

    it("remove method with item in middle of list", () => {
        var testList = new linkedList([1, 2, 3, 4, 5]);
        expect(testList.size()).to.equal(5);
        expect(testList.remove(3)).to.equal(3);
        expect(testList.size()).to.equal(4);
        expect(testList.search(3)).to.throw('This value is not in the LinkedList.');
    });

    it("display method", () => {
        var testList = new linkedList([1, 2, 3, 4, 5]);
        expect(testList.display()).to.be.string('(5, 4, 3, 2, 1)');
    });
});

