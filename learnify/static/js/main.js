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






});

