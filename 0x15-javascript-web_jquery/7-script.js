$.get(
  'https://swapi-api.alx-tools.com/api/people/5/?format=json',
  function (response) {
    $('#character').text(response.name);
  }
);
