#!/usr/bin/node

/*
* Write a script that prints the number of movies where
* the character “Wedge Antilles” is present.
*/


const request = require('request');
const s = require('util');
const URL = 'https://swapi-api.hbtn.io/api/films/';
let count = 0;

request(URL, function (error, res, content) {
  if (error) {
    console.error(error);
  }
  data = JSON.parse(content).results

  // let count = 0;
  for (let movie = 0; movie < data.length; movie++) {

  let list = data[movie].characters;

  for (let idx = 0; idx < list.length; idx++) {

  request(list[idx], function (errorB, resB, contentB) {
    if (errorB) {
      console.error(erroB);
    }
    nameOfCharacter = JSON.parse(contentB).name

    if (nameOfCharacter == "Wedge Antilles") {
      count++;
      console.log(count);
      }
  console.log(movie);
  });
  // console.log(count);
  }
  }
});
