$('document').ready(function(){
    $.get("https://hellosalut.stefanbohacek.dev/?lang=fr", function(data, textStatus){
    $("DIV#hello").html(data.hello);
})

})