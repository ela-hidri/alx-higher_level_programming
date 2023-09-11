#!/usr/bin/node
const argv = process.argv;
const deg = parseInt(argv[2], 10);
let wrd = '';
if (isNaN(deg)) { console.log('Missing size'); } else {
  for (let i = 0; i < deg; i++) {
    for (let i = 0; i < deg; i++) { wrd += 'X'; }
    console.log(wrd);
    wrd = '';
  }
}
