#!/usr/bin/node
const square = require('./5-square');

class Square extends square {
  charPrint (c) {
    for (let i = 0; i < this.height; i++) {
      if (!c) {
        console.log('X'.repeat(this.height));
      } else {
        console.log(c.repeat(this.height));
      }
    }
  }
}

module.exports = Square;
