#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
let data; let temp = 1; let id = 0;
request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    data = JSON.parse(body);
    const result = {};
    data.forEach(function (IdNum) {
      id++;
    });
    while (temp <= id) {
      data.forEach(function (TaskComp) {
        if (TaskComp.userId === temp) {
          if (TaskComp.completed === true) {
            if (result[temp]) {
              result[temp] += 1;
            } else {
              result[temp] = 1;
            }
          }
        }
      });
      temp++;
    }
    console.log(result);
  }
});
