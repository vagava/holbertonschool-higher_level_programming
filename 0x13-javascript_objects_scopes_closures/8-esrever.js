#!/usr/bin/node
exports.esrever = function (list) {
  let size = list.length;
  for (let i = 0; i < size; i++, size--) {
    const aux = list[i];
    list[i] = list[size - 1];
    list[size - 1] = aux;
  }
  return list;
};
