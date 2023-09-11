#!/usr/bin/node
const { argv } = require('process');
const num = parseInt(argv[2]);
function fact (n) {
  if (isNaN(n) || n === 0) {
    return 1;
  }
  return n * fact(n - 1);
}
console.log(fact(num));
