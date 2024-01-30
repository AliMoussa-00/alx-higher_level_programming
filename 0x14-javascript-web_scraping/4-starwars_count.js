#!/usr/bin/node

const request = require('request');
const argv = require('process').argv;

request(argv[2], (err, response, body) => {
  if (err) console.log(err);
  else {
    let count = 0;
    const results = JSON.parse(body).results;
    for (const r of results) {
      const characters = r.characters;
      for (const ch of characters) {
        if (ch.search('18') > 0) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
