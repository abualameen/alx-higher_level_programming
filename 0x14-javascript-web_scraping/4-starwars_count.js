#!/usr/bin/node

const request = require('request');

/**
 * Function to fetch and count the number of movies where the character "Wedge Antilles" (ID 18) is present.
 * @param {string} apiUrl - The API URL of the Star Wars films.
 */
function countMoviesWithWedgeAntilles(apiUrl) {
  request(apiUrl, (error, response, body) => {
    if (error) {
      console.error('Error:', error);
      return;
    }

    if (response.statusCode !== 200) {
      console.error('Unexpected status code:', response.statusCode);
      return;
    }

    try {
      const films = JSON.parse(body).results;
      const count = films.filter((film) => film.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')).length;
      console.log(count);
    } catch (parseError) {
      console.error('Error parsing JSON:', parseError);
    }
  });
}

// Check if the API URL is provided as an argument.
if (process.argv.length !== 3) {
  console.error('Usage: ./4-starwars_count.js <apiUrl>');
  process.exit(1); // Exit with error code 1.
}

// Get the API URL from the command line argument.
const apiUrl = process.argv[2];

// Call the function to fetch and count the number of movies with "Wedge Antilles".
countMoviesWithWedgeAntilles(apiUrl);
