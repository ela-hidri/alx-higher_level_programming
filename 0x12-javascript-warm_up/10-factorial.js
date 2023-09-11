#!/usr/bin/node
const argv = process.argv;
const m = parseInt(argv[2], 10);
function fact (n) {
  if (n === 0) return 1;
  return (n * fact(n - 1));
}
if (isNaN(m)) { console.log(1); } else { console.log(fact(m)); }
