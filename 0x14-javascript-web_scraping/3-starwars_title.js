#!/usr/bin/node
// script that prints the title of a Star Wars movie
// where the episode number matches a given integer.

const ID = process.argv[2];
const URL = 'https://swapi-api.hbtn.io/api/films/' + ID;
const request = require('request');
request(URL, function (err, res, body) {
  if (err) {
    return console.log(err);
  }
  console.log(JSON.parse(body).title);
});
