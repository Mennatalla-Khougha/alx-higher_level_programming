#!/usr/bin/node
const fs = require('fs');
const { argv } = require('process')

const first = argv[2]
const second = argv[3]
const into = argv[4]

fs.readFile(first, (err, date) => {
  if (err) throw err;
  fs.readFile(second, (err, date2) => {
    if (err) throw err;
    const str = date + date2;
    fs.writeFile(into, str, (err) => {
      if (err) throw err;
    });
  });
});
