$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
    for (let i = 0; data.results[i]; i++) {
        $("UL#list_movies").append(("<li>" + data.results[i].title + "</li>"));
    }
});
