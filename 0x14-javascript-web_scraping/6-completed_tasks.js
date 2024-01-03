#!/usr/bin/node

const request = require('request');

/**
 * Function to compute the number of completed tasks by user ID.
 * @param {string} apiUrl - The API URL to request.
 */
function countCompletedTasksByUserId (apiUrl) {
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
      const todos = JSON.parse(body);
      const completedTasksByUserId = {};

      todos.forEach((todo) => {
        if (todo.completed) {
          if (completedTasksByUserId[todo.userId]) {
            completedTasksByUserId[todo.userId] += 1;
          } else {
            completedTasksByUserId[todo.userId] = 1;
          }
        }
      });

      console.log(completedTasksByUserId);
    } catch (parseError) {
      console.error('Error parsing JSON:', parseError);
    }
  });
}

// Check if the API URL is provided as an argument.
if (process.argv.length !== 3) {
  console.error('Usage: ./6-completed_tasks.js <apiUrl>');
  process.exit(1);
}

// Get the API URL from the command line argument.
const apiUrl = process.argv[2];

// Call the function to compute the number of completed tasks by user ID.
countCompletedTasksByUserId(apiUrl);
