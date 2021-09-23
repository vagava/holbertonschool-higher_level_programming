$.getJSON("https://swapi-api.hbtn.io/api/films/?format=json", function (json){
    let array = json.results
    array.forEach(element => {
        let item = $("<li></li>").text(element.title);
        $("#list_movies").append(item)
    });
})
