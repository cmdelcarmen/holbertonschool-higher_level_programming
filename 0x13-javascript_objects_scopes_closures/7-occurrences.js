#!/usr/bin/node

/**
 * Write a function that returns the occurrences in a list:
 */

exports.nbOccurences = function (list, searchElement) {
  let numOfOccurences = 0;

  for (let idx = 0; idx < list.length; idx++) {
    if (list[idx] === searchElement) {
      numOfOccurences++;
    }
  }
  return numOfOccurences;
};
