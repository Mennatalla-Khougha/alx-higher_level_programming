#!/usr/bin/node
const fs = require('fs');

fs.readFile('fileA', (err, date) => {
  if (err) throw err;
  fs.readFile('fileB', (err, date2) => {
    if (err) throw err;
    const str = date + date2;
    fs.writeFile('fileC', str, (err) => {
      if (err) throw err;
    });
  });
});
