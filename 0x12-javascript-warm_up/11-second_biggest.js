#!/usr/bin/node

/*
 * Script that prints the addition of 2 integers
 */

function bblSort (arr) {
  let i;
  let j;
  let temp;

  for (i = 0; i < arr.length; i++) {
    for (j = 0; j < (arr.length - i - 1); j++) {
      if (arr[j] > arr[j + 1]) {
        temp = arr[j];
        arr[j] = arr[j + 1];
        arr[j + 1] = temp;
      }
    }
  }
  console.log(arr);
  console.log(arr[arr.length - 2]);
}

const arg = process.argv;
const array = arg.filter(function parseInt (x) { return (!isNaN(x)); });

if (arg.length <= 2) {
  console.log('0');
} else {
  console.log(array);
  bblSort(array);
}
