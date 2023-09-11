#!/usr/bin/node
const { argv } = require('process');
let num = 0;
argv.forEach((val, index) => {
  if (index === 2) {
    console.log(val);
  }
  num += 1;
});
if (num === 2) {
  console.log('No argument');
}
