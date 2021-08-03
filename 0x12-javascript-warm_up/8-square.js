#!/usr/bin/node
const argv = require('process').argv;

const num = parseInt(argv[2]);

if (isNaN(num)) {
  console.log('Missing size');
} else {
  for (let j = 0; j < num; j++) {
    for (let i = 0; i < num; i++) {
      process.stdout.write('X');
    }
    console.log('');
  }
}
