#!/usr/bin/node
const Arguments = process.argv;
let number = 0;
if (isNaN(Arguments[2])) {
  console.log('Missing number of occurrences');
} else {
  parseInt(Arguments[2]);
  while (number < Arguments[2]) {
    console.log('C is fun');
    number++;
  }
}
