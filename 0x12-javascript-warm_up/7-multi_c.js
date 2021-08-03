#!/usr/bin/node
let i = 0;
let number;
const args = process.argv.slice(2);
if (args[0] === undefined || isNaN(Number(args[0], 10))) {
  console.log('Missing number of occurrences');
} else {
  number = Number(args[0], 10);
  while (i < number) {
    console.log('C is fun');
    i++;
  }
}
