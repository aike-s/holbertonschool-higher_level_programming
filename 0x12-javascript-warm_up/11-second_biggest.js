#!/usr/bin/node
const { argv } = require('process');

argv.sort(function (a, b) { return b - a; });
argv.forEach((val) => {
  console.log(val);
});
console.log(argv[1]);
