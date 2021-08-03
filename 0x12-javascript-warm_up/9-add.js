#!/usr/bin/node
function add (a, b) {
  return (a + b);
}
const argv = require('process').argv;

const sumOfNum = add(parseInt(argv[2]), parseInt(argv[3]));

console.log(sumOfNum);
