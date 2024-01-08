#!/usr/bin/node
const Arguments = process.argv;
let number = 0; let loopNumber = 0;
if (isNaN(Arguments[2])) {
  console.log('Missing size');
} else {
  parseInt(Arguments[2]);
  while (number < Arguments[2]) {
    loopNumber = 0;
    while (loopNumber < Arguments[2]) {
      process.stdout.write('X');
      loopNumber++;
    }
    console.log('');
    number++;
  }
}
