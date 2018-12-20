$(document).ready(function () {
    $('.nav-dropdown').hide();
    $('.nav-profile-pic').on('click', function () {
        $('.nav-dropdown').slideToggle('slow');
    });

    $('.cross').hide();
    $('.hamburger-list').hide();
    $('.hamburger').on('click', function() {
        $('.hamburger-list').slideToggle('slow', function() {
            $('.cross').show();
            $('.hamburger').hide();
        });
    });

    $('.cross').on('click', function() {
        $('.hamburger-list').slideToggle('slow', function() {
            $('.hamburger').show();
            $('.cross').hide();
        });
    });
});

