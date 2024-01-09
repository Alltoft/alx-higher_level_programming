#!/usr/bin/node
let countNumber = 0;
exports.logMe = function (item) {
  console.log(countNumber + ': ' + item);
  countNumber++;
};
