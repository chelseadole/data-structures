'use strict';

var Q = require('../js-que');
var chai = require('chai');
var expect = chai.expect;

describe('js-que.js tests', () => {
    it('creating a new empty Queue', () => {
        var testQ = new Q();
        expect(testQ.size()).to.equal(0);
        expect(testQ.dll.head).to.equal(null);
        expect(testQ.dll.tail).to.equal(null);
    });

    it('passing iterable into new Queue and enqueueing.', () => {
        var testQ = new Q([100, 200, 300, 400, 500]);
        expect(testQ.size()).to.equal(5);
        expect(testQ.dll.head.data).to.equal(500);
        expect(testQ.dll.tail.data).to.equal(100);

    });
 
    it('testing enqueue method changes head', () => {
        var testQ = new Q();
        testQ.enqueue('yo');
        expect(testQ.dll.head.data).to.equal('yo');
        expect(testQ.dll.tail.data).to.equal('yo');
    });

    it('test enqueue method adds one to size.', () => {
        var testQ = new Q();
        testQ.enqueue(1);
        expect(testQ.size()).to.equal(1);
    });

    it("size function works with enqueue and dequeue", () => {
        var testQ = new Q([1, 2, 3, 4, 5]);
        expect(testQ.size()).to.equal(5);
        testQ.enqueue(0);
        expect(testQ.size()).to.equal(6);
        testQ.dequeue();
        expect(testQ.size()).to.equal(5);
    });

    it("dequeue method works on filled queue", () => {
        var testQ = new Q([1, 2, 3, 4, 5]);
        expect(testQ.dequeue()).to.equal(1);
    });

    it("dequeue method changes queue length", () => {
        var testQ = new Q([1, 2, 3, 4, 5]);
        expect(testQ.size()).to.equal(5)
        expect(testQ.dequeue()).to.equal(1);
        expect(testQ.size()).to.equal(4)
    });
});