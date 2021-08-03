#!/usr/bin/node
const { argv } = require('process');

const values = argv.slice(2)
  .sort(function (a, b) { return b - a; });

if (values.length > 1) {
  console.log(values[1]);
} else {
  console.log(0);
}
