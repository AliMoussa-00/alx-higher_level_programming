#!/usr/bin/node

const argv = require('process').argv;
const request = require('request');

function getStatus (starId) {
  const url = `https://swapi-api.alx-tools.com/api/films/${starId}`;
  request.get(url, (error, response, body) => {
    if (error) {
      console.log(error);
      return;
    }
    const data = JSON.parse(body);
    console.log(data.title);
  });
}

if (argv.length >= 3) {
  getStatus(argv[2]);
}
