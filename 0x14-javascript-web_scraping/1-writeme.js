#!/usr/bin/node

const fs = require('fs');
const argv = require('process').argv;

if (argv.length >= 4) {
  const file = argv[2];
  const text = argv[3];

  fs.writeFile(file, text, (err) => {
    if (err) {
      throw (err);
    }
  });
}
