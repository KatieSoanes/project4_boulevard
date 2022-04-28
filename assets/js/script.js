// Reservation button 
// based on 
function reserve()
{
    window.location= "reservation.html"
    setTimeout('myFunction()', 2000);
}

// Scroll to top of page arrow
// code based on W3Schools
mybutton = document.getElementById("btnScrollToTop");

// When the user clicks on the button, scroll to the top of the document
function topFunction() {
  document.body.scrollTop = 0; // For Safari
  document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
}