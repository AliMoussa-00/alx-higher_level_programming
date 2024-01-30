#!/usr/bin/node

const argv = require('process').argv;
const request = require('request');

function getActors (filmId) {
  const filmUrl = `https://swapi-api.alx-tools.com/api/films/${filmId}/`;

  request(filmUrl, (err, response, body) => {
    if (err) {
      console.log(err);
    } else {
      const characters = JSON.parse(body).characters;

      for (const ch of characters) {
        request(ch, (err, response, body) => {
          if (err) {
            console.log(err);
          } else {
            console.log(JSON.parse(body).name);
          }
        });
      }
    }
  });
}

if (argv.length >= 3) {
  getActors(argv[2]);
}
