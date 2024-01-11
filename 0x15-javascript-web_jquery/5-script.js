// 5-script.js

$(document).ready(function() {
    $('#add_item').click(function() {
        const newItem = $('<li></li>').text('Item');
        $('.my_list').append(newItem);
    });
});

