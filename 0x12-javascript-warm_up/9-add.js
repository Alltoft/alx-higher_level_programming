#!/usr/bin/node
const Arguments = process.argv;
if (Arguments[3] === undefined) {
  Arguments[2] = undefined;
} function add () {
  return (parseInt(Arguments[2]) + parseInt(Arguments[3]));
}
console.log(add());
