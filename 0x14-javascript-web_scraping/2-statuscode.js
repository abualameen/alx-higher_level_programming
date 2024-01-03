#!/usr/bin/node

const https = require('https');

/**
 * Function to display the status code of a GET request to a URL.
 * @param {string} url - The URL to request (GET).
 */
function getStatusCode (url) {
  https.get(url, (response) => {
    // Print the status code of the response.
    console.log(`code: ${response.statusCode}`);
  }).on('error', (error) => {
    // If an error occurred during the request, print the error.
    console.error(error);
  });
}

// Check if the URL is provided as an argument.
if (process.argv.length !== 3) {
  console.error('Usage: ./2-statuscode.js <URL>');
  process.exit(1); // Exit with error code 1.
}

// Get the URL from the command line argument.
const url = process.argv[2];

// Call the function to display the status code of the GET request.
getStatusCode(url);
