#!/usr/bin/node
const val = process.argv[2];
const deg = parseInt(val, 10);
if (deg.toString() === 'NaN') { console.log('Not a number'); } else { console.log('My number: ' + val); }
