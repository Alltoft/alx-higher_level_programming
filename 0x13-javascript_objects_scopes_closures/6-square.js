#!/usr/bin/node
const square = require('./5-square');
module.exports = class Square extends square {
  charPrint (c) {
    if (c === undefined) { c = 'X'; }
    {
      let temp = 0; let otherTemp = 0;
      while (temp < this.height) {
        otherTemp = 0;
        while (otherTemp < this.width) {
          process.stdout.write(c);
          otherTemp++;
        }
        console.log('');
        temp++;
      }
    }
  }
};
