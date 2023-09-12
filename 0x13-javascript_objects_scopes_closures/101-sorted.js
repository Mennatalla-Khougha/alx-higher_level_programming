#!/usr/bin/node
const dict = require('./101-data').dict;

const newDict = {};

for (const key in dict) {
  const occurrence = dict[key];

  if (occurrence in newDict) {
    newDict[occurrence].push(key);
  } else {
    newDict[occurrence] = [key];
  }
}
console.log(newDict);
