#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let temp = 0; let retNumber = 0;
  while (temp < list.length) {
    if (list[temp] === searchElement) {
      retNumber++;
    }
    temp++;
  }
  return (retNumber);
};
