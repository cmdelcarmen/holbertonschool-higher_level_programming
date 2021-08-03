#!/usr/bin/node

/*
 * Script prints "My number: <1st arg converted to int>",
 * if the 1st arg can be converted to an int.
 */

const args = process.argv;

if (!(isNaN(args[2]))) {
  console.log('My number: ' + parseInt(args[2]));
} else {
  console.log('Not a number');
}
