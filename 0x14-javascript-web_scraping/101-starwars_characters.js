#!/usr/bin/node

const request = require('request');

const api = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;

request(api, (err, response, body) => {
  if (!err) {
    const characters = JSON.parse(body).characters;
    print(characters, 0);
  }
});

function print (characters, i) {
  request(characters[i], (e, r, b) => {
    if (!e) {
      const char = JSON.parse(b);
      console.log(char.name);
      if (i + 1 < characters.length) {
        print(characters, i + 1);
      }
    }
  });
}
