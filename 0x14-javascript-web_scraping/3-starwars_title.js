#!/usr/bin/node
const request = require('request');
const Arguments = process.argv;
request('https://swapi-api.alx-tools.com/api/films/' + Arguments[2],
  (error, response, body) => {
    if (error) {
      console.error(error);
    } else {
      const JsonRepr = JSON.parse(body);
      const title = JsonRepr.title;
      console.log(title);
    }
  });
