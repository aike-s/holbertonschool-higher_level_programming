#!/usr/bin/node
function factorial (num) {
  if (num == 0) {
    return (1);
  }
  return (num * factorial(num - 1));
}
const argv = require('process').argv;

factorial(argv[2]);
