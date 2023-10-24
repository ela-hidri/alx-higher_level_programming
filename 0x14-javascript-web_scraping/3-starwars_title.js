#!/usr/bin/node
const argv = process.argv;
const request = require('request');
request('https://swapi-api.alx-tools.com/api/films/' + argv[2], function (error, response, body) {
  console.log(JSON.parse(body).title);
  if (error) {
    console.error(error);
  }
});
