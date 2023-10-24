#!/usr/bin/node

const request = require('request');

request(process.argv[2], (err, response, body) => {
  if (!err) {
    const films = JSON.parse(body).results;
    const count = films.reduce((count, movie) => {
      if (movie.characters.find((character) => character.endsWith('/18/'))) {
        count++;
      }
      return count;
    }, 0);
    console.log(count);
  }
});
