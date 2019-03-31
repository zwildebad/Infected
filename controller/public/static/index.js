$(document).ready(function(){
    $("#play").click(function(){
        $("#menu__buttons").css("display", "none");
        $("#login_form").css("display", "grid");
        $("#username").css("display", "block");
        $("#password").css("display", "block");
        $("#login").css("display", "block");
    });
    $("#login").click(function(){
        var toSend = {
            "username": $("#username").value,
            "new_user": $("#new_user").value,
            "password": $("#password").value
        };
        $.post(
            "http://127.0.0.1:3000",
            JSON.stringify(toSend),
            function(){console.log("Connected")},
            "json"
        );
    })
});