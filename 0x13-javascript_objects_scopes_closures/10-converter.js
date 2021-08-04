#!/usr/bin/node
exports.converter = function (base) {
  return function (toConvert) {
    return parseInt(toConvert, 10).toString(base);
  };
};
