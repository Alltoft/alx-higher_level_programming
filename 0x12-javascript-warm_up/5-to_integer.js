#!/usr/bin/node
const Arguments = process.argv;
if (isNaN(Arguments[2])) {
  console.log('Not a number');
} else {
  console.log('My number: ' + parseInt(Arguments[2]));
}
