#!/usr/bin/node

/*
 * Script searches the 2nd biggest int in a list.
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
  console.log(arr[arr.length - 2]);
}

const arg = process.argv;
const array = arg.filter(function (x) { return (!isNaN(x)); });

if (arg.length <= 2) {
  console.log('0');
} else {
  bblSort(array);
}
