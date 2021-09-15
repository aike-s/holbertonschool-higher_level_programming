#!/usr/bin/node
const fileName = process.argv[2];

const fs = require('fs');
fs.readFile(fileName, (error, data) => {
  if (error) {
    console.log(error);
  } else {
    console.log(data.toString());
  }
});
