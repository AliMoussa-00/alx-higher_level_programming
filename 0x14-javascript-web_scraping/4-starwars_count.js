#!/usr/bin/node

const argv = require('process').argv;
const request = require('request');

function getWedgeMovies (url) {
  request.get(url, (error, response, body) => {
    if (error) {
      console.log(error);
      return;
    }
    const films = JSON.parse(body);

    const wedgeId = 'https://swapi-api.alx-tools.com/api/people/18/';
    const wedgeFilms = films.results.filter(film => film.characters.includes(wedgeId));
    console.log(wedgeFilms.length);
  });
}

if (argv.length >= 3) {
  getWedgeMovies(argv[2]);
}
