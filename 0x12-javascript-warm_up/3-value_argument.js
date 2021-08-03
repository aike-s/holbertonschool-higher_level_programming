#!/usr/bin/node
const { argv } = require('process');
if (!(argv[1])) {
  console.log('No argument');
} else {
  console.log(argv[2]);
}
