#!/usr/bin/node
exports.nbOccurences = function (list, c) {
  let occ = 0;
  for (let i = 0; i < list.length; i++) { occ = list[i] === c ? occ + 1 : occ; }
  return occ;
};
