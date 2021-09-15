#!/usr/bin/node

/*
 * Write a script that prints all characters of a Star Wars movie:
 */

const request = require('request');
const films = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request(films, (err, res, body) => {
  if (err) {
    console.error(err);
  }
});
