#!/usr/bin/node
const { argv } = require('process');
const arr = argv.slice(2);
if (arr.length < 2) {
  console.log(0);
} else {
  for (let i = 0; i < arr.length; ++i) {
    arr[i] = parseInt(arr[i]);
  }
  arr.sort((a, b) => b - a);
  console.log(arr[1]);
}
