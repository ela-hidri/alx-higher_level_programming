#!/usr/bin/node
const argv = process.argv;
if (argv.length <= 3) { console.log(0); } else {
  let max = argv[2];
  let sdn;
  for (let i = 3; i < argv.length; i++) {
    if (max < argv[i]) {
      sdn = max;
      max = argv[i];
    } else if (sdn == null) { sdn = argv[i]; }
  }
  console.log(sdn);
}
