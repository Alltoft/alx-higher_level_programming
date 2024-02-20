#!/usr/bin/node
const fs = require('fs');
const Arguments = process.argv;
fs.readFile(Arguments[2], 'utf-8', (err, data) => {
  if (err) {
    console.log(err);
    return;
  }
  console.log(data);
});
