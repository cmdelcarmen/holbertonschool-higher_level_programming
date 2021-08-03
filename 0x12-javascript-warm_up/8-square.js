#!/usr/bin/node

/*
 * Script prints a square
 */

const args = process.argv;
let idx = 0;
let idx2 = 0;
let square = '';

if (isNaN(args[2])) {
  console.log('Missing size');
} else {
  for (idx = 0; idx < parseInt(args[2]); idx++) {
    for (idx2 = 0; idx2 < parseInt(args[2]); idx2++) {
      square += 'X';
    }
    square += '\n';
  }
  console.log(square.slice(0, square.length - 1));
}
