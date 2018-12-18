console.log('I am working');

$(document).ready(function() {
    $('.john').hide();
    $('.forest').on('click', function() {
        $('.john').slideToggle('slow');
    })
});