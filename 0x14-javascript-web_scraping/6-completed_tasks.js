#!/usr/bin/node

const argv = require('process').argv;
const request = require('request');

function getCompletedTasks (url) {
  request.get(url, (error, response, body) => {
    if (error) {
      console.log(error);
      return;
    }

    const tasks = JSON.parse(body);
    const completed = tasks.filter(task => task.completed === true);
    const users = [...new Set(completed.map(task => task.userId))];

    const objects = {};
    for (const user of users) {
      const count = completed.filter(t => t.userId === user).length;

      objects[user] = count;
    }
    console.log(objects);
  });
}

if (argv.length >= 3) {
  getCompletedTasks(argv[2]);
}
