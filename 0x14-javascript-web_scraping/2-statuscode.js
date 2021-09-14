#!/usr/bin/node
// script that display the status code of a GET request.

const URL = process.argv[2];

const request = require('request');
request(URL, function (err, response) {
  if (err) {
    return console.log(err);
  }
  console.log('code:', response && response.statusCode);
});
