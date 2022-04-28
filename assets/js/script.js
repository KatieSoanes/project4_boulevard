// Reservation button 
// based on 
function reserve()
{
    window.location= "reservation.html"
    setTimeout('myFunction()', 2000);
}

// // Scroll to top of page arrow

$(window).scroll(function(){
    if ($(this).btnScrollToTop() > 100) {
        $('.btnScrollToTop').fadeIn();
    } else {
        $('.btnScrollToTop').fadeOut();
    }
});
$('.btnScrollToTop').click(function(){
    $('html, body').animate({scrollTop : 0},800);
    return false;
});