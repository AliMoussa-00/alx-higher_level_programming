$.get(
  "https://swapi-api.alx-tools.com/api/films/?format=json",
  function (response) {
    $.each(response.results, (index, movie) => {
      $("#list_movies").append("<li>" + movie.title + "</li>");
    });
  }
);
