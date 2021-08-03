#!/usr/bin/node
const argv = require('process').argv;

const num = parseInt(argv[2]);

if (isNaN(num)) {
  console.log('Missing size');
} else {
  for (let j = 0; j < num; j++) {
    console.log('X'.repeat(num));
  }
}
