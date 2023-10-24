#!/usr/bin/node
const request = require('request');
const filepath = process.argv[2];
request.get(filepath).on('response', function (response) {
  console.log(`code: ${response.statusCode}`);
});
