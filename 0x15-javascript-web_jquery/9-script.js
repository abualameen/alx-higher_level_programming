// 9-script.js

$(document).ready(function() {
    const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
    $.ajax({
        url: url,
        type: 'GET',
        dataType: 'json',
        success: function(data) {
            $('#hello').text(data.hello);
        },
        error: function(error) {
            console.log('Error:', error);
            $('#hello').text('Error fetching translation.');
        }
    });
});

