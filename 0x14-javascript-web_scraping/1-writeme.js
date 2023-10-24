#!/usr/bin/node

const fs = require('fs');
const filepath = process.argv[2];
const string_content = process.argv[3];
fs.writeFile(filepath, string_content,
  error => {
    if (error) console.log(error);
  });
