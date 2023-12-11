#!/usr/bin/node

const argv = process.argv;

const num = parseInt(argv[2]);

if (isNaN(num) || typeof argv[2] === 'undefined') { console.log('Not a number'); } else { console.log(num); }
