var URL = "classproduct/";
var csrftoken = $("[name=csrfmiddlewaretoken]").val();



$(document).ready(function() {
    $(".update-form").hide()
    $("#adding").click(function() {
        location.href = "/create/";
    });
});



$(document).ready(function() {
    $("#updating").click(function() {
        location.href = "/update/";
    });
});




function getCourses() {
    $.getJSON(URL, {}, showCourses);
}

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
    $("#addressdetails").val(course.addressdetails)
    $("#deleted").val(course.deleted)
}

function showCourses(courses) {


    $(document).ready(function() {
        $(document).on("click", ".editable", function() {
            var value = $(this).text();
            var input = "<input type='text' class='input-data' value='" + value + "' class='form-control'>";
            $(this).html(input);
            $(this).removeClass("editable")
        });

        $(document).on("blur", ".input-data", function(e) {
            var value = $(this).val();
            var td = $(this).parent("td");
            $(this).remove();
            td.html(value);
            td.addClass("editable");
            var type = td.data("type");
            sendToserver(td.data("id"), value);
        });

        $(document).on("keypress", ".input-data", function(e) {
            var key = e.which;
            if (key == 13) {
                var value = $(this).val();
                var td = $(this).parent("td");
                $(this).remove();
                td.html(value);
                td.addClass("editable");
                var type = td.data("type");
                sendToserver(td.data("id"), value);
            }
        });

        function sendToserver(id, value, type) {
            var firstname = value
            console.log(firstname)


        }

    });

    $(document).ready(function() {
        $("#refresh").click(function() {
            location.reload();
        });
    });






    $("#courserows").html("");
    $.each(
        courses,
        function(idx, course) {
            $("#courserows").append(

                "<tr><td><button class='button1' onclick='changes(" + course.id + ")''>Update</button><button id = 'refresh' class='button1' onclick='deleteCourse(" + course.addressdetails + ")'>Delete</button></td><td class='editable' data-id=" + course.id + " data-type='first_name'>" +

                course.first_name +
                "</td><td  class='editable' data-id=" + course.id + " data-type='last_name'>" +
                course.last_name +
                "</td><td class='editable' data-id=" + course.id + " data-type='username'>" +
                course.username +
                "</td><td class='editable' data-id=" + course.id + " data-type='date_of_birth'>" +
                course.date_of_birth +
                "</td><td class='editable' data-id=" + course.id + " data-type='gender'>" +
                course.gender +
                "</td><td class='editable' data-id=" + course.id + " data-type='email_address'>" +
                course.email_address +
                "</td><td class='editable' data-id=" + course.id + " data-type='contact_number'>" +
                course.contact_number +
                "</td><td class='editable' data-id=" + course.id + " data-type='deleted'>" +
                course.deleted +
                "</td><tr>"
            );
        } // anonymous function
    );
    // each()

    $("table_id").show();
    $(document).ready(function() {
        $('#table_id').DataTable({
            ajax: {
                url: URL,
                dataSrc: ""
            },
            columns: [{
                    data: 'action'
                }, {
                    data: 'first_name'
                }, {
                    data: 'last_name'
                }, {
                    data: 'username'
                }, {
                    data: 'date_of_birth'
                }, {
                    data: 'gender'
                }, {
                    data: 'email_address'
                }, {
                    data: 'contact_number'
                }, {
                    data: 'addressdetails'
                }, {
                    data: 'deleted'
                }


            ],
            "pageLength": 3,

        });

    })
} // showCourses
getCourses();

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


function changes(id) {
    $.getJSON("update/classproduct/" + id)
        .done(function(data) {
            $('.employee-table').hide()
            $('.update-form').show()
            console.log(data)
            showCourse(data)

        }) // on success - 200

    .fail(function() // on failure - 404
        {
            alert("Sorry! Course Not Found!");
        }
    );
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

function deleteCourse(id) {
    console.log(id)
    $.ajax({
        "url": URL + id,
        "type": "delete",
        "headers": {
            'csrfmiddlewaretoken': '{{ csrf_token }}'
        },
        "success": delete_success,
        "error": delete_error
    }); // ajax()
}

function delete_success() {
    alert("Deleted Course Successfully");
}

function delete_error() {
    alert("Could not delete Course!");
}