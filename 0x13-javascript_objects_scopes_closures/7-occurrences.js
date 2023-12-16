#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let c = 0;

  list.forEach(elem => {
    elem === searchElement ? c++ : c += 0;
  });

  return c;
};
