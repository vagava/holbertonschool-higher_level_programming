#!/usr/bin/node
const SquareP = require('./5-square');
module.exports = class Square extends SquareP {
  charPrint (c) {
    if (c && typeof c === 'string') {
      for (let i = 0; i < this.height; i++) {
        let row = '';
        for (let j = 0; j < this.width; j++) {
          row += c;
        }
        console.log(row);
      }
    } else {
      this.print();
    }
  }
};
