"use strict";

const LL = require("./js-linked-list")
// import {LL} from "js-linked-list.js"

class Stack {
    constructor(iter=null){
        this.linked = new LL()
        if(Array.isArray(iter)){
            iter.forEach(item => this.push(item))
        }
    }

    size(){
        return this.linked.size()
    }

    push(val){
        this.linked.push(val)
    }

    pop(){
        return this.linked.pop()
    }

}

module.exports = Stack