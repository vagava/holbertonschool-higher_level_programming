#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let ocurrences = 0;
  for (const element in list) {
    if (list[element] === searchElement) {
      ocurrences++;
    }
  }
  return ocurrences;
};
