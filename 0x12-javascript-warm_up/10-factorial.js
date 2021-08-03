#!/usr/bin/node
function factorial (num) {
  if (isNaN(num) || !num || num <= 0) {
    return (1);
  }
  return (num * factorial(num - 1));
}
const argv = require('process').argv;

console.log(factorial(argv[2]));
