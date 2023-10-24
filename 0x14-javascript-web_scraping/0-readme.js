#!/usr/bin/node
const argv = process.argv;
const fs = require('fs');
fs.readFile(argv[2], 'utf8', function (err, data) {
  if (err) throw err;
  console.log(data);
});
