window.onload = function () {
  $('#btn_translate').click(function () {
    const lang = $('#language_code').val();
    const url = 'https://hellosalut.stefanbohacek.dev/?lang=' + lang;

    $.get(url, function (response) {
      $('#hello').text(response.hello);
    });
  });
};
