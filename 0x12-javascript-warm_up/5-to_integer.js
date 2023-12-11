#!/usr/bin/node

const argv = process.argv;

const num = Math.floor(Number(process.argv[2]));

console.log(isNaN(num) ? 'Not a number' : `'My number:' ${num}`)
