#!/usr/bin/node
const argmentsNumber = process.argv;
if (argmentsNumber[2] !== undefined) {
  console.log(argmentsNumber[2]);
} else {
  console.log('No argument');
}
