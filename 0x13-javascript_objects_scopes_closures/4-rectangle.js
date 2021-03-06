#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let idx = 0;
    let idx2 = 0;
    let rectangle = '';

    for (idx = 0; idx < this.height; idx++) {
      for (idx2 = 0; idx2 < this.width; idx2++) {
        rectangle += 'X';
      }
      rectangle += '\n';
    }
    console.log(rectangle.slice(0, rectangle.length - 1));
  }

  rotate () {
    const temp = this.height;

    this.height = this.width;
    this.width = temp;
  }

  double () {
    this.height *= 2;
    this.width *= 2;
  }
}

module.exports = Rectangle;
