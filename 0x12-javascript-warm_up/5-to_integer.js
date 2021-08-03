#!/usr/bin/node
const argv = require('process').argv;

const num = parseInt(Number(argv[2]));

if (isNaN(num)) {
  console.log('Not number');
} else {
  console.log('My number: ' + num);
}
