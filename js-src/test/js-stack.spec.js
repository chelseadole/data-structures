'use strict';

var Stack = require('../js-stack');
var chai = require('chai');
var expect = chai.expect;

describe('stack.js tests', () => {
    it('creating a new empty Stack', () => {
        var testStack = new Stack();
        expect(testStack.size()).to.equal(0);
        expect(testStack.linked.head).to.equal(null);
    });

    it('passing iterable into new Stack and pushing.', () => {
        var testStack = new Stack([100, 200, 300, 400, 500]);
        expect(testStack.size()).to.equal(5);
        expect(testStack.linked.head.data).to.equal(500);

    });
 
    it('testing push method changes head', () => {
        var testStack = new Stack();
        testStack.push('yo');
        expect(testStack.linked.head.data).to.equal('yo');
    });

    it('test push method adds one to size.', () => {
        var testStack = new Stack();
        testStack.push(1);
        expect(testStack.size()).to.equal(1);
    });

    it("test pop on non-empty list.", () => {
        var testStack = new Stack();
        testStack.push(5);
        testStack.push(4);
        testStack.push(3);
        expect(testStack.linked.head.data).to.equal(3);
        expect(testStack.pop()).to.equal(3);
        expect(testStack.linked.head.data).to.equal(4);
    });

    it("size function works with push and pop", () => {
        var testStack = new Stack([1, 2, 3, 4, 5]);
        expect(testStack.size()).to.equal(5);
        testStack.push(0);
        expect(testStack.size()).to.equal(6)
        testStack.pop();
        expect(testStack.size()).to.equal(5);
    });
});
