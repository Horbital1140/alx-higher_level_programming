#!/usr/bin/node

const fs = require('fs');
const filepath = process.argv[2];
fs.readFile(filepath, 'utf8', function (error, content) {
  console.log(error || content);
});
