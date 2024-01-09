#!/usr/bin/node
let countNumber = 0;
exports.logMe = function (item) {
  countNumber++;
  console.log(countNumber + ': ' + item);
};
