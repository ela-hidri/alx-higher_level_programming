#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let wrd = '';
    for (let i = 0; i < this.height; i++) {
      for (let i = 0; i < this.width; i++) { wrd += 'X'; }
      console.log(wrd);
      wrd = '';
    }
  }

  rotate () {
    const aux = this.height;
    this.height = this.width;
    this.width = aux;
  }

  double () {
    this.height = 2 * this.height;
    this.width = 2 * this.width;
  }
};
