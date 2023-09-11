#!/usr/bin/node
const argv = process.argv;
const deg = parseInt(argv[2], 10);
if (isNaN(deg)) { console.log('Missing number of occurrences'); } else { for (let i = 0; i < deg; i++) { console.log('C is fun'); } }
