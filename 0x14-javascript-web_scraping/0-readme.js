#!/usr/bin/node

/*
* Write a script that reads and prints the content of a file
*/

const process = require('process');
const fs = require('fs');
const file = process.argv[2];

fs.readFile(file, 'utf8', (error, fileContent) => {
  if (error) {
    console.error(error);
    return;
  }
  console.log(fileContent);
});
