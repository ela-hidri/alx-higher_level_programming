#!/usr/bin/node
const argv = process.argv;
if (argv.length <= 3) { console.log(0); } else {
  argv.sort((a, b) => a - b);
  console.log(argv[argv.length - 2]);
}
