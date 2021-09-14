#!/usr/bin/node
// script that reads and prints the content of a file.
file = process.argv[2];
fs = require('fs');
fs.readFile(file, 'utf-8', function (err, data) {
  if (err) {
    return console.log(err);
  }
  console.log(data);
});
