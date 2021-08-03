#!/usr/bin/node

const args = process.argv.slice(2);
if (args[0] === undefined) {
  console.log('Not a number');
} else if (isNaN(Number(args[0], 10))) {
  console.log('Not a number');
} else {
  console.log(Number(args[0], 10));
}
