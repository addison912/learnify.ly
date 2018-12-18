console.log('I am working');

$(document).ready(function () {
    $('.nav-dropdown').hide();
    $('.forest').on('click', function () {
        $('.nav-dropdown').slideToggle('slow');
    })
});