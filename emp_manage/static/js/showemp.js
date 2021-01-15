var URL = "classproduct/";
var URL1 = "update/classproduct/";
// var csrftoken = $("[name=csrfmiddlewaretoken]").val();



function getCookie(name) {

    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

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
        $("#refresh").click(function() {
            location.reload();
        });
        $('#view').click(function() {
            $('#first_name').attr("disabled", "disabled");
            $('#last_name').attr("disabled", "disabled");
            $('#username').attr("disabled", "disabled");
            $('#date_of_birth').attr("disabled", "disabled");
            $('#gender').attr("disabled", "disabled");
            $('#email_address').attr("disabled", "disabled");
            $('#contact_number').attr("disabled", "disabled");
            $('#addressdetails').attr("disabled", "disabled");
            $('#address_line_1').attr("disabled", "disabled");
            $('#address_line_2').attr("disabled", "disabled");
            $('#city').attr("disabled", "disabled");
            $('#country').attr("disabled", "disabled");
            $('#pincode').attr("disabled", "disabled");

            document.getElementById('update-butt').style.visibility = 'hidden';
        });



        $(".update").hide()
        $(".delete").hide()
        $(".update-inner").hide()
        $("#adding").hide()
        set_permissions()



    });

    function set_permissions() {
        var get_permissions = localStorage.getItem("permissions")
        var permissions = JSON.parse(get_permissions)
        console.log(permissions)
            // if (permissions.includes("view_employees")) {
            //     $(".update").show()

        // }
        // 

        if (permissions.includes("change_employees")) {
            $(".update").show()

        }
        if (permissions.includes("delete_employees")) {
            $(".delete").show()

        }
        if (permissions.includes("change_employees")) {
            $(".update-inner").show()

        }

        if (permissions.includes("add_employees")) {
            $("#adding").show()

        }


    }






    $("#courserows").html("");
    $.each(
        courses,
        function(idx, course) {
            $("#courserows").append(

                "<tr><td><button class='button1 update' onclick='changes(" + course.id + ")'>Update</button><button id = 'refresh' class='button1 delete' onclick='deleteCourse(" + course.addressdetails + ")'>Delete</button><buttons class='button1' id='view' onclick='changes1(" + course.id + ")'>View</buttons></td><td class='editable' data-id=" + course.id + " data-type='first_name'>" +

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

function changes1(id) {
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


function updateCourse(e) {
    console.log(e)
    $.ajax({

        "url": "/update-employee/" + $("#addressdetails").val(),
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
            'csrfmiddlewaretoken': $(".add-employee").find('input[name=csrfmiddlewaretoken]').val()
        },
        "type": "post",
        "contentType": 'application/json',
        "headers": {
            "X-CSRFToken": $(".update-employee").find('input[name=csrfmiddlewaretoken]').val()

        },
        "success": update_success,
        "error": update_error
    }); // ajax()
    return False;
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
        "data": {
            'csrfmiddlewaretoken': getCookie("csrftoken")
        },
        "headers": {
            'X-CSRFToken': getCookie("csrftoken")
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