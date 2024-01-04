#!/usr/bin/node

const request = require('request');

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
      const expectedOrder = [
        'C-3PO', 'R2-D2', 'Darth Vader', 'Leia Organa', 'Obi-Wan Kenobi',
        'Chewbacca', 'Han Solo', 'Jabba Desilijic Tiure', 'Wedge Antilles',
        'Yoda', 'Palpatine', 'Boba Fett', 'Lando Calrissian', 'Ackbar',
        'Mon Mothma', 'Arvel Crynyd', 'Wicket Systri Warrick', 'Nien Nunb',
        'Bib Fortuna'
      ];
      const fetchedCharacters = [];

      const fetchCharacter = (url) => new Promise((resolve, reject) => {
        request(url, (charError, charResponse, charBody) => {
          if (!charError && charResponse.statusCode === 200) {
            const characterData = JSON.parse(charBody);
            fetchedCharacters.push(characterData.name);
            resolve();
          } else {
            reject(charError || new Error('Failed to fetch character'));
          }
        });
      });

      Promise.all(charactersUrls.map(url => fetchCharacter(url)))
        .then(() => {
          expectedOrder.forEach(expectedName => {
            if (!fetchedCharacters.includes(expectedName)) {
              console.log('Characters not found');
              console.log(fetchedCharacters);
              process.exit(1);
            }
          });
          console.log('OK');
        })
        .catch(err => {
          console.error('Error fetching characters:', err);
          process.exit(1);
        });

    } catch (parseError) {
      console.error('Error parsing JSON:', parseError);
      process.exit(1);
    }
  });
}

if (process.argv.length !== 3) {
  console.error('Usage: ./101-starwars_characters.js <movieId>');
  process.exit(1);
}

const movieId = process.argv[2];
getStarWarsCharacters(movieId);
