#!/usr/bin/node
// script that display the status code of a GET request.

const URL = process.argv[2];

const https = require('https');
https.get(URL, function (res) {
  console.log('code: ', res.statusCode);
});
