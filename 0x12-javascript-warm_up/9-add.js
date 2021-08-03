#!/usr/bin/node

/*
 * Script that prints the addition of 2 integers
 */

const args = process.argv;
let sum = 0;

if (isNaN(args[2]) || isNaN(args[3])) {
  console.log('NaN');
} else {
  sum = parseInt(args[2]) + parseInt(args[3]);
  console.log(sum);
}
