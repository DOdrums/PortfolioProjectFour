$('.navbar-collapse').on('hide.bs.collapse', function() {
    $('.hero-image').css('margin-top', '-99px')
});

$('.navbar-collapse').on('show.bs.collapse', function() {
    console.log("on showing");
    $('.hero-image').css('margin-top', '0px')
});