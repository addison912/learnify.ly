console.log('I am working');

$(document).ready(function () {
    $('.nav-dropdown').hide();
    $('.nav-profile-pic').on('click', function () {
        $('.nav-dropdown').slideToggle('slow');
    })
});
