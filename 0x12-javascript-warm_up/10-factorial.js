#!/usr/bin/node

function factorial (a) {
  if (a === 1) {
    return 1;
  } else {
    return factorial(a - 1) * a;
  }
}

const args = process.argv.slice(2);
if (args[0] === undefined || isNaN(Number(args[0], 10))) {
  console.log(1);
} else {
  console.log(factorial(Number(args[0], 10)));
}
