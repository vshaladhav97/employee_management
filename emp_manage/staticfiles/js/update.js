var URL = "classproduct/";
var csrftoken = $("[name=csrfmiddlewaretoken]").val();


function getCourse() {
    $.getJSON(URL + $("#id").val())
        .done(showCourse) // on success - 200
        .fail(function() // on failure - 404
            {
                alert("Sorry! Course Not Found!");
            }
        );
}

function showCourse(course) {
    $("#id").val(course.id)
    $("#first_name").val(course.first_name)
    $("#last_name").val(course.last_name)
    $("#username").val(course.username)
    $("#date_of_birth").val(course.date_of_birth)
    $("#gender").val(course.gender)
    $("#email_address").val(course.email_address)
    $("#contact_number").val(course.contact_number)
    $("#addressdetails").val(course.addressdetails),
        $("#address_line_1").val(course.addressdetails__address_line_1),
        $("#address_line_2").val(course.addressdetails__address_line_2),
        $("#city").val(course.addressdetails__city),
        $("#country").val(course.addressdetails__country),
        $("#pincode").val(course.addressdetails__pincode),
        $("#deleted").val(course.addressdetails__deleted)
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
            "addressdetails": $("#addressdetails").val(),
            "address_line_1": $("#address_line_1").val(),
            "address_line_2": $("#address_line_2").val(),
            "city": $("#city").val(),
            "country": $("#country").val(),
            "pincode": $("#pincode").val(),
            "deleted": $("#deleted").val()
        },
        "type": "post",
        "headers": {
            "X-CSRFToken": '{{ csrf_token }}'
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

function updateCourse() {
    $.ajax({
        "url": URL + $("#id").val(),
        "data": {
            "id": $("#id").val(),
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
        },
        "type": "put",
        "headers": {
            "X-CSRFToken": '{{ csrf_token }}'
        },
        "success": update_success,
        "error": update_error
    }); // ajax()
}

function update_success() {
    alert("Updated Course Successfully");
}

function update_error() {
    alert("Could not update Course!");
}