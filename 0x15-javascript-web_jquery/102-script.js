window.onload = function () {
  $("#btn_translate").click(function () {
    lang = $("#language_code").val();
    let url = "https://hellosalut.stefanbohacek.dev/?lang=" + lang;

    $.get(url, function (response) {
      $("#hello").text(response.hello);
    });
  });
};
