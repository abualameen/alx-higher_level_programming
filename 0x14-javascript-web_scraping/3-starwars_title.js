#!/usr/bin/node

const request = require('request');

/**
 * Function to fetch and print the title of a Star Wars movie by its ID.
 * @param {number} movieId - The ID of the Star Wars movie.
 */
function getMovieTitle (movieId) {
  const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

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
      const movieData = JSON.parse(body);
      console.log(movieData.title);
    } catch (parseError) {
      console.error('Error parsing JSON:', parseError);
    }
  });
}

// Check if the movie ID is provided as an argument.
if (process.argv.length !== 3) {
  console.error('Usage: ./3-starwars_title.js <movieId>');
  process.exit(1); // Exit with error code 1.
}

// Get the movie ID from the command line argument.
const movieId = process.argv[2];

// Call the function to fetch and print the title of the Star Wars movie.
getMovieTitle(movieId);
