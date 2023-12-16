#!/usr/bin/node

const fs = require('fs');

if (process.argv.length === 5) {
  const f1 = process.argv[2];
  const f2 = process.argv[3];
  const dest = process.argv[4];

  try {
    const data1 = fs.readFileSync(f1, 'utf8');
    const data2 = fs.readFileSync(f2, 'utf8');

    fs.writeFileSync(dest, data1 + data2);
  } catch (err) {
    console.error(err);
  }
}
