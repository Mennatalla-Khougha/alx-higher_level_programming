#!/usr/bin/node

const request = require('request');

const api = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;

request(api, (err, response, body) => {
  if (!err) {
    const film = JSON.parse(body);
    film.characters.forEach(character => {
      request(character, (e, r, b) => {
        if (!e) {
          const char = JSON.parse(b);
          console.log(char.name);
        }
      });
    });
  }
});
