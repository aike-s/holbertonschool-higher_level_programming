#!/usr/bin/node
const fileName = process.argv[3];
const url = process.argv[2];

const fs = require('fs');
const request = require('request');

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    fs.writeFile(fileName, body, (error) => {
      if (error) {
        console.log(error);
      }
    });
  }
});
