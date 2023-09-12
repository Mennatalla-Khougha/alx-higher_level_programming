#!/usr/bin/node
class Rectangle {
  width;
  height;

  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(`${this.width}`));
    }
  }

  rotate () {
    const tmp = this.height;
    // return(this.height, tmp)
    this.height = this.width;
    this.width = tmp;
  }

  double () {
    this.width = 2 * this.width;
    this.height = 2 * this.height;
  }
}

module.exports = Rectangle;
