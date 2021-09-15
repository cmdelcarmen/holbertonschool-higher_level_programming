#!/usr/bin/node
const request = require('request');
const films = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request(films, (err, res, body) => {
  if (err) {
    console.error(err);
    return;
  }
});
