#!/usr/bin/node

const list = require('./100-data').list;

const mapped = list.map((elem, index) => (elem * index));

console.log(list);
console.log(mapped);
