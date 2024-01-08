#!/usr/bin/node
const argmentsNumber = process.argv.length - 2;
if (argmentsNumber === 0) {
  console.log('No argument');
} else if (argmentsNumber === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
