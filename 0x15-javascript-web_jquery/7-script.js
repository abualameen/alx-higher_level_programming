// 7-script.js

$(document).ready(function() {
    const url = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';
    $.ajax({
        url: url,
        type: 'GET',
        dataType: 'json',
        success: function(data) {
            $('#character').text(data.name);
        },
        error: function(error) {
            console.log('Error:', error);
            $('#character').text('Error fetching character name.');
        }
    });
});

