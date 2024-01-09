#!/usr/bin/node
exports.esrever = function (list) {
  let temp = list.length - 1;
  const tempolist = [];
  while (temp >= 0) {
    tempolist.push(list[temp]);
    temp--;
  }
  return (tempolist);
};
