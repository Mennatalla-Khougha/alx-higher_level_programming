#!/usr/bin/node
const request = require('request');

request(process.argv[2], (err, response, body) => {
  if (!err) {
    const doneTasks = {};
    const todo = JSON.parse(body);

    todo.forEach((task) => {
      if (task.completed) {
        const userId = task.userId;
        if (doneTasks[userId]) {
          doneTasks[userId]++;
        } else {
          doneTasks[userId] = 1;
        }
      }
    });
    console.log(doneTasks);
  }
});
