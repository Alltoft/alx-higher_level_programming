#!/usr/bin/node
exports.converter = function (base) {
  return function convertednumber (num) {
    return num.toString(base);
  };
};
