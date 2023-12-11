#!/usr/bin/node

const { argv } = require('node:process');

const n = parseInt(argv[2]);

function factorial (i) {
  if (isNaN(i) || i === 1) { return (1); } else { return i * factorial(i - 1); }
}

console.log(factorial(n));
