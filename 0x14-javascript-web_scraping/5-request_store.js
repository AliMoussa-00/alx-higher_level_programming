#!/usr/bin/node

const argv = require('process').argv;
const fs = require('fs');
const request = require('request');

if (argv.length >= 4) {
  const url = argv[2];
  const file = argv[3];

  request
    .get(url)
    .on('error', err => { console.error(err); })
    .pipe(fs.createWriteStream(file));
}
