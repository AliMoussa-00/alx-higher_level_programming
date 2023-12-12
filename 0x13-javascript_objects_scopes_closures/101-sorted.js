#!/usr/bin/node

const dict = require('./101-data').dict;

const sorted = {};

Object.entries(dict).forEach((arr) => {
  let tmp = [];

  if (Object.hasOwn(sorted, arr[1])) {
    tmp = sorted[arr[1]];
  }

  tmp.push(arr[0]);
  sorted[arr[1]] = tmp;
});

console.log(sorted);
