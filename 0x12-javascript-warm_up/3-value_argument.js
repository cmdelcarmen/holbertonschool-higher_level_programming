#!/usr/bin/node

/*
 * Script prints first argument passed to it.
 */

const args = process.argv;

if (args.length <= 2) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
