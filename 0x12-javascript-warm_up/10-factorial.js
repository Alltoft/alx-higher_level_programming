#!/usr/bin/node
const Arguments = process.argv;
if (isNaN(Arguments[2])) {
  Arguments[2] = 1;
} function factorial () {
  let number = Arguments[2];
  let retNumber = 1;
  while (parseInt(number) > 0) {
    retNumber *= parseInt(number);
    number--;
  }
  return (retNumber);
}
console.log(factorial());
