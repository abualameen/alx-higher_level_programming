// 8-script.js

$(document).ready(function() {
    const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';
    $.ajax({
        url: url,
        type: 'GET',
        dataType: 'json',
        success: function(data) {
            data.results.forEach(function(movie) {
                const listItem = $('<li></li>').text(movie.title);
                $('#list_movies').append(listItem);
            });
        },
        error: function(error) {
            console.log('Error:', error);
            $('#list_movies').append('<li>Error fetching movies.</li>');
        }
    });
});

