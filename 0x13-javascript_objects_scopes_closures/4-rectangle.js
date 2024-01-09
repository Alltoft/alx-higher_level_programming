#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    } else {
      Object.create(null);
    }
  }

  print () {
    let temp = 0; let otherTemp = 0;
    while (temp < this.height) {
      otherTemp = 0;
      while (otherTemp < this.width) {
        process.stdout.write('X');
        otherTemp++;
      }
      console.log('');
      temp++;
    }
  }

  rotate () {
    let temp = 0;
    temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
};
