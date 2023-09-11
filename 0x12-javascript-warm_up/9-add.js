#!/usr/bin/node
const argv = process.argv;
const n1 = parseInt(argv[2], 10);
const n2 = parseInt(argv[3], 10);
function add (a, b) { return (a + b); }
console.log(add(n1, n2));
