#!/usr/bin/node

const fs = require('fs');
const argv = require('process').argv;

if (argv.length >= 3) {
  const file = argv[2];

  fs.readFile(file, 'utf8', (err, data) => {
    if (err) {
      console.error(err);
    } else console.log(data.toString());
  });
}
