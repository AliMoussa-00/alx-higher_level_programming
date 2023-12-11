#!/usr/bin/node

const { argv } = require('node:process');

const num = parseInt(argv[2]);

if (isNaN(num) || typeof argv[2] === 'undefined') { console.log('Missing number of occurrences'); } else {
  let i = 0;
  while (i < num) {
    console.log('C is fun');
    i++;
  }
}
