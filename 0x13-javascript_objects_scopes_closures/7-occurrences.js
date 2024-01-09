#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
    let temp = 0, retNumber = 0;
    while (temp < list.length) {
       if (list[temp] === searchElement) {
        retNumber++;
       }
       temp++;
    }
    return(retNumber)
}
