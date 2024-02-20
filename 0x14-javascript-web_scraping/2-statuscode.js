#!/usr/bin/node
const request = require('request');
const Arguments = process.argv;
request(Arguments[2], (error, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('code:', response.statusCode);
  }
});
