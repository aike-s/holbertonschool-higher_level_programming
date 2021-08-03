#!/usr/bin/node
const addMeMaybe = function (number, theFunction) {
  theFunction(number + 1);
};
exports.addMeMaybe = addMeMaybe;
