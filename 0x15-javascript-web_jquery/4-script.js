$("DIV#toggle_header").on("click", function(){
    if ($("header").hasClass("red")){
        $("header").removeClass("red");
        $("header").addClass("green");
    } else if($("header").hasClass("green")){
        $("header").addClass("red");
        $("header").removeClass("green");
    }
});