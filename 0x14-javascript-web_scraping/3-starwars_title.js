#!/usr/bin/node

const request = require('request');

const api = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;
request(api, (err, response, body) => {
  if (err) {
    console.log(err);
  }
  console.log(JSON.parse(body).title);
});
