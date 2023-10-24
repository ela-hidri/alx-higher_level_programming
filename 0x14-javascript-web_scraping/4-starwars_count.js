#!/usr/bin/node
const argv = process.argv;
const request = require('request');
request(argv[2], function (error, response, body) {
  const nb = JSON.parse(body).results.filter((elem) => {
    return elem.characters.filter((url) => { return url.includes('/18'); }).length;
  }).length;
  console.log(nb);
  if (error) {
    console.error(error);
  }
});
