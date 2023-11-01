$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
  const movies = data.results;
  $.each(movies, function (index, movie) {
    const name = movie.title;
    const list = $('<li>').text(name);
    $('UL#list_movies').append(list);
  });
});
