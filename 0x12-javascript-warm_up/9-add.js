#!/usr/bin/node
const { argv } = require('process');
const firstNum = parseInt(argv[2]);
const secondNum = parseInt(argv[3]);
function add (a, b) {
  return (a + b);
}
console.log(add(firstNum, secondNum));
