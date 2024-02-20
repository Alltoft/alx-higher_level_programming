#!/usr/bin/node
const fs = require('fs');
const Arguments = process.argv;
fs.writeFile(Arguments[2], Arguments[3], 'utf-8', (err, data) => {
  if (err) {
    console.log(err);
    return;
  }
  console.log(data);
});
