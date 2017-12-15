'use strict';

var DLL = require('../js-doubly-linked-list');
var chai = require('chai');
var expect = chai.expect;

describe('js-doubly-linked-list.js tests', () => {
    it('creating a new empty DLL', () => {
        var testList = new DLL();
        expect(testList.size()).to.equal(0);
        expect(testList.head).to.equal(null);
        expect(testList.tail).to.equal(null);
    });

    it('passing iterable into new LinkedList and pushing.', () => {
        var testList = new DLL([100, 200, 300, 400, 500]);
        expect(testList.size()).to.equal(5);
        expect(testList.head.data).to.equal(500);
        expect(testList.tail.data).to.equal(100);

    });
 
    it('testing push method changes head', () => {
        var testList = new DLL();
        testList.push('yo');
        expect(testList.head.data).to.equal('yo');
        expect(testList.tail.data).to.equal('yo');
    });

    it('test push method adds one to size.', () => {
        var testList = new DLL();
        testList.push(1);
        expect(testList.size()).to.equal(1);
    });

    it("test pop on non-empty list.", () => {
        var testList = new DLL();
        testList.push(5);
        testList.push(4);
        testList.push(3);
        expect(testList.head.data).to.equal(3);
        expect(testList.pop()).to.equal(3);
        expect(testList.head.data).to.equal(4);
    });

    it("size function works with push and pop", () => {
        var testList = new DLL([1, 2, 3, 4, 5]);
        expect(testList.size()).to.equal(5);
        testList.push(0);
        expect(testList.size()).to.equal(6);
        testList.pop();
        expect(testList.size()).to.equal(5);
    });

    it("search on list without searched value", () => {
       var testList = new DLL();
       testList.push(5);
       expect(testList.search(2)).to.equal('This value is not in the LinkedList.');
    });

    it('correct search method works', () => {
        var testList = new DLL();
        testList.push(5);
        testList.push(4);
        expect(testList.search(5).data).to.equal(5);
    });

    it("remove method with item in head of list", () => {
        var testList = new DLL();
        testList.push(1);
        expect(testList.size()).to.equal(1);
        expect(testList.remove(1)).to.equal(1);
        expect(testList.size()).to.equal(0);
    });

    it("remove method with item in middle of list", () => {
        var testList = new DLL([1, 2, 3, 4, 5]);
        expect(testList.size()).to.equal(5);
        expect(testList.remove(3)).to.equal(3);
        expect(testList.size()).to.equal(4);
        expect(testList.search(3)).to.equal('This value is not in the LinkedList.');
    });

    it("append method works on filled list", () => {
        var testList = new DLL([1, 2, 3]);
        expect(testList.size()).to.equal(3);
        testList.append(4);
        expect(testList.size()).to.equal(4);
        expect(testList.tail.data).to.equal(4);
    });

    it("append method works on empty list", () => {
        var testList = new DLL();
        expect(testList.size()).to.equal(0);
        testList.append(100);
        expect(testList.size()).to.equal(1);
        expect(testList.tail.data).to.equal(100);
        expect(testList.head.data).to.equal(100);

    });

    it("shift method doesnt work on empty list", () => {
        var testList = new DLL();
        expect(testList.shift()).to.equal('Cannot shift() from empty DLL.');
    });

    it("shift method works on filled list", () => {
        var testList = new DLL([1, 2, 3, 4, 5]);
        expect(testList.shift()).to.equal(1);
    });

    it("shift method changes list length", () => {
        var testList = new DLL([1, 2, 3, 4, 5]);
        expect(testList.size()).to.equal(5)
        expect(testList.shift()).to.equal(1);
        expect(testList.size()).to.equal(4)

    });

    it("display method", () => {
        var testList = new DLL([1, 2, 3, 4, 5]);
        expect(testList.display()).to.be.string('(5, 4, 3, 2, 1)');
    });
});
