#!/iusr/bin/node

/*
 * Write a script that computes the number of tasks completed by user id.
 */

const req = require('request');
const urlAPI = process.argv[2];

req(urlAPI, (error, res, content) => {
  if (error) {
    console.error(error);
    return;
  }

  const taskList = JSON.parse(content);
  const completedTasks = {};

  for (const task of taskList) {
    if (task.completed) {
      const user_id = task.userId;
      completedTasks[user_id] = (completedTasks[user_id] + 1 || 1);
    }
  }
  console.log(completedTasks);
});
