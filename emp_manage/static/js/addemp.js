var URL = "classproduct/";
// var csrftoken = $("[name=csrfmiddlewaretoken]").val();

// function getCookie(name) {
//     var cookieValue = null;

//     if (document.cookie && document.cookie != '') {
//         var cookie = document.cookie.split(';');

//         for (var i = 0; i < cookie.length; i++) {
//             var cookie = cookies[i].trim();

//             if (cookie.substring(0, name.length + 1) === (name + '=')) {
//                 cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
//                 break;
//             }
//         }
//     }
//     return cookieValue;
// };

// var csrfToken = getcookie('csrftoken')


$(document).ready(function() {
    $("#backview").click(function() {
        location.href = "/";
    });
});

function getCourse() {
    $.getJSON(URL + $("#addressdetails").val())
        .done(showCourse) // on success - 200
        .fail(function() // on failure - 404
            {
                alert("Sorry! Course Not Found!");
            }
        );
}

function showCourse(course) {
    $("#first_name").val(course.first_name)
    $("#last_name").val(course.last_name)
    $("#username").val(course.username)
    $("#date_of_birth").val(course.date_of_birth)
    $("#gender").val(course.gender)
    $("#email_address").val(course.email_address)
    $("#contact_number").val(course.contact_number)
    $("#address_line_1").val(course.address_line_1),
        $("#address_line_2").val(course.address_line_2),
        $("#city").val(course.city),
        $("#country").val(course.country),
        $("#pincode").val(course.pincode),
        $("#deleted").val(course.deleted)
}

function addCourse() {

    $.ajax({
        "url": URL,
        "data": {
            "first_name": $("#first_name").val(),
            "last_name": $("#last_name").val(),
            "username": $("#username").val(),
            "date_of_birth": $("#date_of_birth").val(),
            "gender": $("#gender").val(),
            "email_address": $("#email_address").val(),
            "contact_number": $("#contact_number").val(),
            "address_line_1": $("#address_line_1").val(),
            "address_line_2": $("#address_line_2").val(),
            "city": $("#city").val(),
            "country": $("#country").val(),
            "pincode": $("#pincode").val(),
            "deleted": $("#deleted").val(),
            'csrfmiddlewaretoken': $(".add-employee").find('input[name=csrfmiddlewaretoken]').val()

        },
        "type": "post",
        "headers": {
            "X-CSRFToken": $(".add-employee").find('input[name=csrfmiddlewaretoken]').val()

        },
        "success": add_success,
        "error": add_error

    }); // ajax()

}

function add_success() {
    alert("Added course Successfully");
}

function add_error() {
    alert("Could not add course!");
}