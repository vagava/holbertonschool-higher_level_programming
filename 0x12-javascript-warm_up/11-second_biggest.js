#!/usr/bin/node

const args = process.argv.slice(2);
const arrayNumbers = [];
let i;

if (args[0] === undefined || args.length === 1 || isNaN(Number(args[0], 10))) {
  console.log(0);
} else {
  for (i = 0; i < args.length; i++) {
    arrayNumbers.push(Number(args[i], 10));
  }
  arrayNumbers.sort();
  arrayNumbers.reverse();
  console.log(arrayNumbers[1]);
}
