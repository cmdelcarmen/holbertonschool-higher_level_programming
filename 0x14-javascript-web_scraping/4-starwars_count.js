#!/usr/bin/node

/*
 Write a script that prints the number of movies where the character “Wedge Antilles” is present.*
 */

const request = require('request');
const urlAPI = process.argv[2];
const characterID = 18;
const characterUrl = 'https://swapi-api.hbtn.io/api/people/' + characterID + '/';

request(urlAPI, (error, res, content) => {
  if (error) {
    console.error(error);
    return;
  }
  const data = JSON.parse(content).results;

  let numberOfMovies = 0;
  for (const movie of data) {
    for (const character of movie.characters) {
      if (character === characterUrl) {
        numberOfMovies++;
      }
    }
  }
  console.log(numberOfMovies);
});
