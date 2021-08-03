#!/usr/bin/node

/*
 * Script prints a square
 */

const args = process.argv;
let idx = 0;
let idx2 = 0;

if (isNaN(args[2])) {
  console.log('Missing size');
} else {
  for (idx = 0; idx < parseInt(args[2]); idx++) {
    for (idx2 = 0; idx2 < parseInt(args[2]); idx2++) {
      process.stdout.write('x');
    }
    console.log();
  }
}
