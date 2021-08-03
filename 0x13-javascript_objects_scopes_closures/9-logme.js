#!/usr/bin/node
const listItems = [];

exports.logMe = function (item) {
  listItems.push(item);
  console.log((listItems.length - 1) + ': ' + listItems.slice(-1).pop());
};
