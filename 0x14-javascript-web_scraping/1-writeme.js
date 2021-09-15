#!/usr/bin/node
const fileName = process.argv[2];
const fileContent = process.argv[3];
const fs = require('fs');

fs.writeFile(fileName, fileContent, (error) => {
  if (error) {
    console.log(error);
  }
});
