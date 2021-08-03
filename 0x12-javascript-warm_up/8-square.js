#!/usr/bin/node
let i = 0;
let j = 0;
let number;
let row = '';
const args = process.argv.slice(2);
if (args[0] === undefined || isNaN(Number(args[0], 10))) {
  console.log('Missing size');
} else {
  number = Number(args[0], 10);
  while (i < number) {
    while (j < number) {
      row += 'X';
      j++;
    }
    console.log(row);
    i++;
  }
}
