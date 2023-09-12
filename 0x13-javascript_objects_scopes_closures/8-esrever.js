#!/usr/bin/node
exports.esrever = function (list) {
  let rev = [];
  rev = list.reduce((a, i) => [i].concat(a), []);
  return rev;
};
