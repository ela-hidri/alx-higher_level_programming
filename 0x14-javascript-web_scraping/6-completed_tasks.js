#!/usr/bin/node
const argv = process.argv;
const request = require('request');
request(argv[2], function (error, response, body) {
  const tb = {};
  const todos = JSON.parse(body);
  todos.forEach(t => {
    if (t.completed) {
      if (tb[t.userId] === undefined) { tb[t.userId] = 1; } else {
        tb[t.userId] = tb[t.userId] + 1;
      }
    }
  });
  console.log(tb);
  if (error) {
    console.error(error);
  }
});
