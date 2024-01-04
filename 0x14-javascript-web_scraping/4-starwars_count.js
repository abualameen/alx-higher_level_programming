#!/usr/bin/node

const request = require('request');

/**
 * Function to count the number of movies where the character "Wedge Antilles" (ID 18) is present.
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
      const count = films.filter(film => {
        // Check each character's URL to see if it contains the ID for Wedge Antilles
        return film.characters.some(charUrl => charUrl.includes('/18/'));
      }).length;

      console.log(count);
    } catch (parseError) {
      console.error('Error parsing JSON:', parseError);
    }
  });
}

if (process.argv.length !== 3) {
  console.error('Usage: ./4-starwars_count.js <apiUrl>');
  process.exit(1);
}

const apiUrl = process.argv[2];
countMoviesWithWedgeAntilles(apiUrl);
