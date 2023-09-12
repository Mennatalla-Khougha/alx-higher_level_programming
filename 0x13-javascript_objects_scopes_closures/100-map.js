#!/usr/bin/node
const list = require('./100-data').list;

const lst = list.map((val, i) => val * i);
console.log(list);
console.log(lst);
