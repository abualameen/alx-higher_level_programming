#!/usr/bin/node
const fs = require('fs');

const [, , sourceFile1, sourceFile2, destinationFile] = process.argv;

if (!sourceFile1 || !sourceFile2 || !destinationFile) {
  console.error('Usage: ./102-concat.js sourceFile1 sourceFile2 destinationFile');
  process.exit(1);
}

let content1 = '';
let content2 = '';

try {
  content1 = fs.readFileSync(sourceFile1, 'utf-8').trim(); // Trim to remove extra whitespace
} catch (error) {
  console.error(`Error reading ${sourceFile1}: ${error.message}`);
  process.exit(1);
}

try {
  content2 = fs.readFileSync(sourceFile2, 'utf-8').trim(); // Trim to remove extra whitespace
} catch (error) {
  console.error(`Error reading ${sourceFile2}: ${error.message}`);
  process.exit(1);
}

let concatenatedContent;

if (content1.length === 0 && content2.length === 0) {
  concatenatedContent = '';
} else if (content1.length === 0) {
  concatenatedContent = content2;
} else if (content2.length === 0) {
  concatenatedContent = content1;
} else {
  concatenatedContent = `${content1}\n${content2}\n`;
}

fs.writeFileSync(destinationFile, concatenatedContent);
