#!/usr/bin/node

/**
 * Write a function that returns the reversed version of a list.
 * Not allowed to use built in func 'reverse'
 */

exports.esrever = function (list) {
  const revList = [];

  for (let idx = (list.length - 1); idx >= 0; idx--) {
    revList.push(list[idx]);
  }
  return revList;
};
