#!/usr/bin/node
const argv = process.argv;
const fs = require('fs');
const request = require('request');
request(argv[2]).pipe(fs.createWriteStream(argv[3]));
