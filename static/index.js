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
        $.ajax({
            url: "http://127.0.0.1:5000",
            data: JSON.stringify(toSend),
            dataType: 'json',
            contentType: 'application/json; charset=utf-8',
            async: false
        });
    })
});