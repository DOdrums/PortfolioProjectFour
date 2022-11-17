// code taken from https://stackoverflow.com/a/70415401/16545052
// script to properly collapse navbar on homepage.
$('.navbar-collapse').on('hide.bs.collapse', function() {
    $('.hero-image').css('margin-top', '-99px');
});

$('.navbar-collapse').on('show.bs.collapse', function() {
    console.log("on showing");
    $('.hero-image').css('margin-top', '0px');
});