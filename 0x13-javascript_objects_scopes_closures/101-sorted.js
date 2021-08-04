#!/usr/bin/node
const { dict } = require('./101-data');
const newDict = {};

for(let key in dict) {
  const value = dict[key];
  newDict[value];
  if(newDict[value] === undefined) {
    newDict[value] = [];
  }
  newDict[value].push(key);
}

console.log(newDict);
