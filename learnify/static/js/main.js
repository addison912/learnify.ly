$(document).ready(function () {
    $('.nav-profile-pic').on('click', function () {
        $('.nav-dropdown').slideToggle('slow');
    });

    $('.hamburger').on('click', function () {
        $('.cross').show();
        $('.hamburger').hide();
        $('.hamburger-list').slideToggle('slow', function () {
        });
    });

    $('.cross').on('click', function () {
        $('.hamburger').show();
        $('.cross').hide();
        $('.hamburger-list').slideToggle('slow', function () {
        });
    });
<<<<<<< HEAD
    
=======

    $("#course-edit-submit").on("submit", (e) => {
        e.preventDefault;
        let id = $("#course-edit-submit").attr("data-id")
        $.ajax({
            method: "PUT",
            url: `/course/${id}/edit_course`,
            success: editCourseSuccess(id),
            error: editCourseError
        });
    });
>>>>>>> 34dfbd9ed6d29aa85420895b492b8f82f0427a12
});

function editCourseSuccess(id) {
    console.log("successfully edited course")
    window.location.replace(`/courses/${id}`);
}

function editCourseError() {
    console.log("failed to edit course")
}

