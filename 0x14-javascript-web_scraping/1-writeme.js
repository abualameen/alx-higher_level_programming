#!/usr/bin/node

const fs = require('fs');

/**
 * Function to write a string to a file.
 * @param {string} filePath - The path of the file to write.
 * @param {string} content - The content to write to the file.
 */
function writeToFile (filePath, content) {
  fs.writeFile(filePath, content, 'utf-8', (err) => {
    if (err) {
      console.error(err);
      return;
    }
    console.log('The file has been saved!');
  });
}

if (process.argv.length !== 4) {
  console.error('Usage: ./1-writeme.js <file-path> <content>');
  process.exit(1);
}
const filePath = process.argv[2];
const content = process.argv[3];
writeToFile(filePath, content);
