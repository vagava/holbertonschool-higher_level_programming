#!/usr/bin/node
function add (a, b) {
  return Number(a) + Number(b);
}

const args = process.argv.slice(2);

if (args[0] === undefined || args[1] === undefined ||
  isNaN(Number(args[0], 10)) || isNaN(Number(args[1], 10))) {
  console.log('NaN');
} else {
  console.log(add(args[0], args[1]));
}
