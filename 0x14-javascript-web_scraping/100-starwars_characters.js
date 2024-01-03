#!/usr/bin/node

const request = require('request');

/**
 * Function to fetch and print all characters of a Star Wars movie by Movie ID.
 * @param {string} movieId - The ID of the Star Wars movie.
 */
function getStarWarsCharacters(movieId) {
  const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

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
      const charactersUrls = movieData.characters;
      charactersUrls.forEach((characterUrl) => {
        request(characterUrl, (charError, charResponse, charBody) => {
          if (!charError && charResponse.statusCode === 200) {
            const characterData = JSON.parse(charBody);
            console.log(characterData.name);
          } else {
            console.error('Error fetching character:', charError);
          }
        });
      });
    } catch (parseError) {
      console.error('Error parsing JSON:', parseError);
    }
  });
}
if (process.argv.length !== 3) {
  console.error('Usage: ./100-starwars_characters.js <movieId>');
  process.exit(1);
}
const movieId = process.argv[2];
getStarWarsCharacters(movieId);
