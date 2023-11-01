$.get("https://swapi-api.alx-tools.com/api/films/?format=json", function(data, textStatus){
    data.results.forEach(element => {
        $("UL#list_movies").append("<li>"+element.title+"</li>");
    });    

})