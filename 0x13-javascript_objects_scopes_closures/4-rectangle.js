#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let row = '';
      for (let j = 0; j < this.width; j++) {
        row += 'X';
      }
      console.log(row);
    }
  }

  rotate () {
    for (let i = 0; i < this.width; i++) {
      let row = '';
      for (let j = 0; j < this.height; j++) {
        row += 'X';
      }
      console.log(row);
    }
  }

  double () {
    for (let i = 0; i < this.height * 2; i++) {
      let row = '';
      for (let j = 0; j < this.width * 2; j++) {
        row += 'X';
      }
      console.log(row);
    }
  }
};
