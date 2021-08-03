#!/usr/bin/node

/*
 * Script prints x times 'C is fun'
 */

const args = process.argv;
let idx = 0;

if (isNaN(args[2])) {
  console.log('Missing number of occurrences');
} else {
  for (idx = 0; idx < parseInt(args[2]); idx++) {
    console.log('C is fun');
  }
}
