#!/usr/bin/node

const request = require('request');

function getStarWarsCharacters (movieId) {
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

      const fetchCharacter = (url) => new Promise((resolve, reject) => {
        request(url, (charError, charResponse, charBody) => {
          if (!charError && charResponse.statusCode === 200) {
            const characterData = JSON.parse(charBody);
            resolve({ order: charactersUrls.indexOf(url), name: characterData.name });
          } else {
            reject(charError || new Error('Failed to fetch character'));
          }
        });
      });

      Promise.all(charactersUrls.map(url => fetchCharacter(url)))
        .then(characters => {
          characters.sort((a, b) => a.order - b.order).forEach(character => {
            console.log(character.name);
          });
        })
        .catch(err => console.error('Error fetching characters:', err));
    } catch (parseError) {
      console.error('Error parsing JSON:', parseError);
    }
  });
}

if (process.argv.length !== 3) {
  console.error('Usage: ./101-starwars_characters.js <movieId>');
  process.exit(1);
}

const movieId = process.argv[2];
getStarWarsCharacters(movieId);
