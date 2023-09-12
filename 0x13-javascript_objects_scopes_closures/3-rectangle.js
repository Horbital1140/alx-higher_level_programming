#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if ((h > 0) && (w > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let b = 0; b < this.height; b++) {
      let b = '';
      for (let c = 0; c < this.width; c++) {
        b += 'x';
      }
      console.log(b);
    }
  }
}

module.exports = Rectangle;
