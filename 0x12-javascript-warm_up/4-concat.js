#!/usr/bin/node

/*
 * Script prints two arguments passed to it,
 * in the following format: "is".
 */

const args = process.argv;
const str = args[2] + ' is ' + args[3];

console.log(str);
