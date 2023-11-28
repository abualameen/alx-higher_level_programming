#!/usr/bin/node
const fs = require('fs');

const [, , sourceFile1, sourceFile2, destinationFile] = process.argv;

if (!sourceFile1 || !sourceFile2 || !destinationFile) {
  console.error('Usage: ./102-concat.js sourceFile1 sourceFile2 destinationFile');
  process.exit(1);
}

const content1 = fs.readFileSync(sourceFile1, 'utf-8').trim(); // Trim to remove extra whitespace
const content2 = fs.readFileSync(sourceFile2, 'utf-8').trim(); // Trim to remove extra whitespace

const concatenatedContent = `${content1}\n${content2}\n`;

fs.writeFileSync(destinationFile, concatenatedContent);
