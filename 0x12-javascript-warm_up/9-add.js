#!/usr/bin/node

const { argv } = require('node:process');

const a = parseInt(argv[2]);
const b = parseInt(argv[3]);

function add (a, b) {
  return (a + b);
}

const num = add(a, b);

console.log(num);
