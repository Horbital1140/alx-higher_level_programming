#!/usr/bin/node
const fs = require('fs');
const filepath = process.argv[2];
const stringContent = process.argv[3];
fs.writeFile(filepath, stringContent,
  error => {
    if (error) console.log(error);
  });
