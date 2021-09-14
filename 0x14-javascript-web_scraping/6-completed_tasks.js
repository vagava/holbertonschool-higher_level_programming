#!/usr/bin/node
// script that computes the number of tasks completed by user id.

const URL = process.argv[2];

const request = require('request');
request(URL, function (err, res, body) {
  if (err) {
    return console.log(err);
  }
  const allUserAndTask = JSON.parse(body);
  const taskDoneByUser = {};
  let count = 0;
  for (let i = 1; i <= 10; i++) {
    count = 0;
    for (const j of allUserAndTask) {
      if (j.userId === i && j.completed === true) {
        count++;
      }
    }
    if (count !== 0) {
      taskDoneByUser[i] = count;
    }
  }
  console.log(taskDoneByUser);
});
