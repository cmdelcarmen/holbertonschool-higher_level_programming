#!/usr/bin/node

function factorial (n) {
  if (n < 0 || n === 0) { return (1); } else {
    return (n * factorial(n - 1));
  }
}

const args = process.argv;

if (isNaN(args[2])) {
  console.log('1');
} else {
  console.log(factorial(args[2]));
}
