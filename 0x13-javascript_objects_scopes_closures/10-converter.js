#!/usr/bin/node
let b;
exports.converter = function (base) {
  b = base;
  return convert;
};

function convert (arr) {
  return arr.toString(b);
}
