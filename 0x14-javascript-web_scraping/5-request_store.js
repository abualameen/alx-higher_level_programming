#!/usr/bin/node

const request = require('request');
const fs = require('fs');

/**
 * Function to fetch the contents of a webpage and store it in a file.
 * @param {string} url - The URL to request.
 * @param {string} filePath - The file path to store the body response.
 */
function requestAndStore (url, filePath) {
  request(url, (error, response, body) => {
    if (error) {
      console.error('Error:', error);
      return;
    }

    if (response.statusCode !== 200) {
      console.error('Unexpected status code:', response.statusCode);
      return;
    }

    // Write the body response to the specified file path with UTF-8 encoding.
    fs.writeFile(filePath, body, 'utf-8', (writeError) => {
      if (writeError) {
        console.error('Error writing to file:', writeError);
      }
    });
  });
}

// Check if the URL and file path are provided as arguments.
if (process.argv.length !== 4) {
  console.error('Usage: ./5-request_store.js <URL> <filePath>');
  process.exit(1);
}

// Get the URL and file path from the command line arguments.
const url = process.argv[2];
const filePath = process.argv[3];

// Call the function to fetch the contents of the webpage and store it in the file.
requestAndStore(url, filePath);
