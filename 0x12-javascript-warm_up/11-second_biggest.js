#!/usr/bin/node
const Arguments = process.argv;
let bigNumber = 0, secbigNumber = 0, loopNumber = 2;
if (Arguments[2] === undefined || Arguments.length === 3) {
    console.log(0);
} else  {
    console.log('I am here');
    while (parseInt(loopNumber) < Arguments.length)   {
        console.log('I am here');
        if (parseInt(secbigNumber) < Arguments[loopNumber])  {
            if (parseInt(bigNumber) < Arguments[loopNumber])
                bigNumber = Arguments[loopNumber];
            else
                secbigNumber = Arguments[loopNumber];
        }
        else {
            continue;
        }
        loopNumber++;
    }
}
console.log(secbigNumber);
