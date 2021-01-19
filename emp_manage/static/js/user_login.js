function login() {
    $.ajax({
        "url": "",
        "data": {

            "username": $("#id_username").val(),
            "password": $("#id_password").val(),
            'csrfmiddlewaretoken': $(".forms").find('input[name=csrfmiddlewaretoken]').val()
        },
        "type": "post",
        "headers": {
            "X-CSRFToken": $(".forms").find('input[name=csrfmiddlewaretoken]').val()
        },
        "success": RedirectHomePage,
        "error": function(data) {
            alert("Sorry! user not found");
        }

    }); // ajax()

}

function RedirectHomePage(data) {

    localStorage.setItem("permissions", JSON.stringify(data.perm))
    window.location = "http://127.0.0.1:8000/"

}