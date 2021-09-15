#!/usr/bin/node

/*
* Write a script that display the status code of a GET request.
*/

const process = require('process');
const request = require('request');
const s = require('util');
const movieID = process.argv[2];
const URL = s.format('https://swapi-api.hbtn.io/api/films/%s', movieID);

console.log(URL);

request(URL, function (error, res, content) {
  if (error) {
    console.error(error);
  }
  console.log(JSON.parse(content).title);
});
