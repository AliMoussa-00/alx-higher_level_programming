#!/usr/bin/node

exports.esrever = function (list) {
  const arr = [];

  list.forEach(elem => {
    arr.unshift(elem);
  });

  return (arr);
};
