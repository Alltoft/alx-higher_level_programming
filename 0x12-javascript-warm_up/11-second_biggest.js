#!/usr/bin/node
const Arguments = process.argv.map(Number);
let bigNumber = 0; let secbigNumber = 0; let loopNumber = 2; const length = Arguments.length;
if (Arguments[2] === undefined || Arguments.length < 4) {
  console.log(0);
} else {
  while (loopNumber < length) {
    if (secbigNumber < Arguments[loopNumber]) {
      if (bigNumber < Arguments[loopNumber]) {
        secbigNumber = bigNumber;
        bigNumber = Arguments[loopNumber];
      } else { secbigNumber = Arguments[loopNumber]; }
    }
    loopNumber++;
  }
  console.log(secbigNumber);
}
