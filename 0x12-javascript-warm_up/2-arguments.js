#!/usr/bin/node
/*
 * Script prints a message depending of the number arguments passed
 */

import { argv } from 'process';

let args = process.argv[2];
console.log(args);
