#!/usr/bin/node
// script that gets the contents of a webpage and stores it in a file.
const URL = process.argv[2];
const path = process.argv[3];

const request = require('request');
const fs = require('fs');

request(URL, function (err, res, body) {
  if (err) {
    return console.log(err);
  }
  fs.writeFileSync(path, body);
});
