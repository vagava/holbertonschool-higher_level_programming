#!/usr/bin/node
// script that writes a string to a file.
const file = process.argv[2];
const message = process.argv[3];
const fs = require('fs');
// first way
fs.writeFileSync(file, message);

// second way
// fs.writeFile(file, message, function(err) {
//   if(err) {
//       return console.log(err);
//   }
//   console.log("The file was saved!");
