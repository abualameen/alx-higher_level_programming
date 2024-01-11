// 102-script.js

$(document).ready(function() {
  $('#btn_translate').click(function() {
    const languageCode = $('#language_code').val();
    $.get(`https://www.fourtonfish.com/hellosalut/hello/?lang=${languageCode}`, function(data) {
      const helloTranslation = data.hello;
      $('#hello').text(helloTranslation);
    }).fail(function() {
      $('#hello').text('Error fetching translation.');
    });
  });

});

