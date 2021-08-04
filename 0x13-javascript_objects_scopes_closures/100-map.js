#!/usr/bin/node
const listCompute = require('./100-data').list;
const arrayToComputed = listCompute.map((x, i) => x * i);
console.log(listCompute);
console.log(arrayToComputed);
