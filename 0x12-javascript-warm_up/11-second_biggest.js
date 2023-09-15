#!/usr/bin/node

function secondLargest (arr) {
  arr = arr.map(Number);
  if (arr.length < 2) {
    return 0;
  }

  let first = -Infinity;
  let second = -Infinity;

  for (const num of arr) {
    if (num > first) {
      second = first;
      first = num;
    } else if (num > second && num !== first) {
      second = num;
    }
  }
  return second;
}

const args = process.argv.slice(2);
const result = secondLargest(args);

console.log(result);
