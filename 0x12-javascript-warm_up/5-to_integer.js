#!/usr/bin/node
const { argv } = require('process');
if (argv.length < 3 || isNaN(Number(argv[2]))) {
  console.log('Not a number');
} else {
  console.log(`My number: ${parseInt(argv[2])}`);
}
