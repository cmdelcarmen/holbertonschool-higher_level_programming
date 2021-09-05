#!/usr/bin/node

/**
 * Write a class Square that defines a square
 * and inherits from Square of 5-square.js.
 */

const SquareNew = require('./5-square');

class Square extends SquareNew {
  charPrint (c) {
    for (let idx = 0; idx < this.height; idx++) {
      if (c === undefined) {
        console.log('X'.repeat(this.width));
      } else {
        console.log(c.repeat(this.width));
      }
    }
  }
}
module.exports = Square;
