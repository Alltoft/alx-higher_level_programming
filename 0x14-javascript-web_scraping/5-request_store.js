#!/usr/bin/node
const fs = require('fs');
const request = require('request');
const Arguments = process.argv;
request(Arguments[2], (error, response) => {
  if (error) {
    console.error(error);
  } else {
    fs.writeFile(Arguments[3], response.body, 'utf-8', err => {
      if (err) {
        console.log(err);
      }
    });
  }
});
