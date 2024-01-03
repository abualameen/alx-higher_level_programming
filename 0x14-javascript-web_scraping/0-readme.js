#!/usr/bin/node

const fs = require('fs');

/**
 * Function to read and print the content of a file.
 * @param {string} filePath - The path of the file to read.
 */
function readFileContent (filePath) {
  fs.readFile(filePath, 'utf-8', (err, data) => {
    if (err) {
      console.error(err);
      return;
    }
    console.log(data);
  });
}
if (process.argv.length !== 3) {
  console.error('Usage: ./0-readme.js <file-path>');
  process.exit(1);
}
const filePath = process.argv[2];
readFileContent(filePath);
