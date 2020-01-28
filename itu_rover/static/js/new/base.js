$(document).ready(function(){
//$("#bg").css({left: "-30%"});

$("#bg").animate({width: "120%", left: "-10%", top: "-20%"}, 500, function(){});
/*
    // ---------------------------------UP - DOWN--------------------------------
    $("#first-btn").click(function(){
        $(".content").animate({top: "0"});
    });
    $("#second-btn").click(function(){
        $(".content").animate({top: "-100%"});
    });
    $("#third-btn").click(function(){
        $(".content").animate({top: "-200%"});
    });
    $("#fourth-btn").click(function(){
        $(".content").animate({top: "-300%"});
    });
*/
    $("#first-btn").click(function(){
        $("#_1").animate({top: "0"});
        $("#_2").animate({top: "0"});
        $("#_3").animate({top: "0"});
        $("#_4").animate({top: "-100"});
    });
    $("#second-btn").click(function(){
        $("#_1").animate({top: "-100%"});
        $("#_2").animate({top: "-100%"});
        $("#_3").animate({top: "-100%"});
        $("#_4").animate({top: "-0%"});
    });
    $("#third-btn").click(function(){
        $("#_1").animate({top: "-200%"});
        $("#_2").animate({top: "-200%"});
        $("#_3").animate({top: "-200%"});
        $("#_4").animate({top: "-100%"});
    });
    $("#fourth-btn").click(function(){
        $("#_1").animate({top: "-300%"});
        $("#_2").animate({top: "-300%"});
        $("#_3").animate({top: "-300%"});
        $("#_4").animate({top: "-200%"});
    });

    $("#mobile").click(function(){
        $(".inner-nav div").slideToggle({"display": "block"});
    });

});