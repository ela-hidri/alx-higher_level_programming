#!/usr/bin/node
const argv = process.argv;
const fs = require('fs');
fs.writeFile(argv[2], argv[3], err => {
  if (err) {
    console.error(err);
  }
});
