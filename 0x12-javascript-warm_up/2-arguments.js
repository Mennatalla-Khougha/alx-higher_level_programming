#!/usr/bin/node
const { argv } = require('process');
let num = 0;
argv.forEach((val, index) => {
  num += 1;
});
if (num === 2) {
  console.log('No argument');
} else if (num === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
