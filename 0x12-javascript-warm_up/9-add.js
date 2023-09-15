#!/usr/bin/node

function add (a, b) {
  return parseInt(a) + parseInt(b);
}

const first = process.argv[2];
const second = process.argv[3];

if (isNaN(first) || isNaN(second)) {
  console.log('MaN');
} else {
  console.log(add(first, second));
}
