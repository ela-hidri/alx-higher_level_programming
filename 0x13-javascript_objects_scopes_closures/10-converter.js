#!/usr/bin/node
exports.converter = function (base) {
  return arr => arr.toString(base);
};
