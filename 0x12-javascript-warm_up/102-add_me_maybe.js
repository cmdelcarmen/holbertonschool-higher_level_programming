#!/usr/bin/node

module.exports.addMeMaybe = function addMeMaybe (n, f) {
  n++;
  f(n);
};
