#!/usr/bin/node
const request = require('request');
const Arguments = process.argv;
const IDs = 8; let temp = 1; let EpNum = 0;
while (temp < IDs) {
  request(Arguments[2] + '/' + temp, (error, response, body) => {
    if (error) {
      console.error(error);
    } else {
      const toJson = JSON.parse(body);
      const charactr = toJson.characters;
      for (const url of charactr) {
        if (url.endsWith('18/')) {
          EpNum++;
        }
      }
    }
  });
  temp++;
}
setTimeout(() => {
  console.log(EpNum);
}, 10000);
