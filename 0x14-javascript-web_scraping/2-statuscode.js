#!/usr/bin/node

const request = require('request');

/**
 * Function to display the status code of a GET request to a URL.
 * @param {string} url - The URL to request (GET).
 */
function getStatusCode (url) {
  request(url, (error, response) => {
    if (error) {
      console.error(error);
      return;
    }
    console.log(`code: ${response.statusCode}`);
  });
}
if (process.argv.length !== 3) {
  console.error('Usage: ./2-statuscode.js <URL>');
  process.exit(1);
}

// Get the URL from the command line argument.
const url = process.argv[2];

// Call the function to display the status code of the GET request.
getStatusCode(url);
