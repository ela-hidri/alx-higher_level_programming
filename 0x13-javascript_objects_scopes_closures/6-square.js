#!/usr/bin/node
const Squaree = require('./5-square');
module.exports = class Square extends Squaree {
  constructor (size) { super(size); }

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
