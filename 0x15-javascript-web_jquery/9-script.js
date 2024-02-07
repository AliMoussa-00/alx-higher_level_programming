$.get("https://hellosalut.stefanbohacek.dev/?lang=fr", function (response) {
  $("#hello").text(response.hello);
});
