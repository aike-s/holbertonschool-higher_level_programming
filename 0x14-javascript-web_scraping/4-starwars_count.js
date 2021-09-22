#!/usr/bin/node
const numAntilles = 0;
let i = 0;

for (let id = 1; id <= 7; id++) {
  const url = process.argv[2] + '/' + id;
  const request = require('request');
  request(url, function (error, response, body) {
    if (error) {
      console.log(error);
    } else {
      charactersList = (JSON.parse(body).characters);
      while (charactersList[i]) {
        if (i === 17) { numAntilles++; } else { i++; }
        console.log('miau' + id);
      }
    }
  });
}
console.log(numAntilles);
