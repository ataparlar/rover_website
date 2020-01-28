$(document).ready(function(){
//$("#bg").css({left: "-30%"});

$("#bg").animate({width: "120%", left: "-10%", top: "-20%"}, 500, function(){});

    // ---------------------------------UP - DOWN--------------------------------

    $("#first-btn").click(function(){
        $("#_1").animate({top: "0"});
        $("#_2").animate({top: "0"});
    });
    $("#second-btn").click(function(){
        $("#_1").animate({top: "-100%"});
        $("#_2").animate({top: "-100%"});
    });

    $("#mobile").click(function(){
        $(".inner-nav div").slideToggle({"display": "block"});
    });

});