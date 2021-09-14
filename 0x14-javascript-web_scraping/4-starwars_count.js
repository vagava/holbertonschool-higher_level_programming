#!/usr/bin/node
//  script that prints the number of movies where the
// character “Wedge Antilles” is present.

const characterID = '18/';
const URL = process.argv[2];

const request = require('request');
request(URL, function (err, res, body) {
  if (err) {
    return console.log(err);
  }
  const results = JSON.parse(body).results;
  let totalMovies = 0;
  for (let i = 0; i < results.length; i++) {
    const listCharacters = results[i].characters;
    if (listCharacters.some(findCharacter)) {
      totalMovies++;
    }
  }
  console.log(totalMovies);
});

function findCharacter (value, index, array) {
  return value === 'https://swapi-api.hbtn.io/api/people/' + characterID;
}
