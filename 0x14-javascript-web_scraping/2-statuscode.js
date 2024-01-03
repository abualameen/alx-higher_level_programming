#!/usr/bin/node

const https = require('https');

/**
 * Function to display the status code of a GET request to a URL.
 * @param {string} url - The URL to request (GET).
 */
function getStatusCode(url) {
  const options = {
    followRedirect: true, // Enable following redirects
  };

  https.get(url, options, (response) => {
    if (response.statusCode >= 300 && response.statusCode < 400 && response.headers.location) {
      getStatusCode(response.headers.location);
    } else {
      console.log(`code: ${response.statusCode}`);
    }
  }).on('error', (error) => {
    console.error(error);
  });
}
if (process.argv.length !== 3) {
  console.error('Usage: ./2-statuscode.js <URL>');
  process.exit(1);
}
const url = process.argv[2];.
getStatusCode(url);
