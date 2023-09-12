#!/usr/bin/node
const Rectangle = require('./4-rectangle');
module.exports = class Square extends Rectangle {
  constructor (size) { super(size, size); }

  charPrint (c) {
    if (typeof c === 'undefined') { this.print(); } else {
      let wrd = '';
      for (let i = 0; i < this.height; i++) {
        for (let i = 0; i < this.width; i++) { wrd += c; }
        console.log(wrd);
        wrd = '';
      }
    }
  }
};
