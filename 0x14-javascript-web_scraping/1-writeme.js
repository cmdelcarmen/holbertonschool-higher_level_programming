#!/usr/bin/node

/*
* Write a script that writes a string to a file.
*/

const process = require('process');
const fs = require('fs');
const file = process.argv[2];
const dataForFile = process.argv[3];

fs.writeFile(file, dataForFile, function (error) {
  if (error) {
    console.error(error);
  }
});
