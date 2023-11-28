#!/usr/bin/node
const fs = require('fs');

const [, , sourceFile1, sourceFile2, destinationFile] = process.argv;

if (!sourceFile1 || !sourceFile2 || !destinationFile) {
  console.error('Usage: ./102-concat.js sourceFile1 sourceFile2 destinationFile');
  process.exit(1);
}

const content1 = fs.readFileSync(sourceFile1, 'utf-8').trim();
const content2 = fs.readFileSync(sourceFile2, 'utf-8').trim();

let concatenatedContent;

if (content1.length === 0) {
  concatenatedContent = content2;
} else if (content2.length === 0) {
  concatenatedContent = content1;
} else {
  concatenatedContent = `${content1}\n${content2}\n`;
}

fs.writeFileSync(destinationFile, concatenatedContent);
