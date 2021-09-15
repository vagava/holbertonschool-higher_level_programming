#!/usr/bin/node
// script that prints all characters of a Star Wars movie.
const ID = process.argv[2];
const URL = 'https://swapi-api.hbtn.io/api/films/' + ID;

const request = require('request');
request(URL, function (err, res, body) {
  if (err) {
    return console.log(err);
  }
  const characters = JSON.parse(body).characters;
  for (let i = 0; i < characters.length; i++) {
    request(characters[i], function (err, res, body) {
      if (err) {
        return console.log(err);
      }
      console.log(JSON.parse(body).name);
    });
  }
});
