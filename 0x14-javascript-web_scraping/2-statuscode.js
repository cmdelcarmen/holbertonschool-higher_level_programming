#!/usr/bin/node

/*
* Write a script that display the status code of a GET request.
*/

const process = require('process');
const request = require('request');
const URL = process.argv[2];

request(URL, function (error, res, content) {
  if (error) {
    console.error(error);
  }
  console.log("code:", res.statusCode);
});
