$.getJSON("https://fourtonfish.com/hellosalut/?lang=fr", function (json){
   $("#hello").text(json.hello)
})
