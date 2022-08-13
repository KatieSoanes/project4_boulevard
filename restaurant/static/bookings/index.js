//const boo = JSON.parse(document.getElementById('value').textContent);
//console.log(boo)
window.makeBooking= function() {
    var form = document.getElementById('booking-form')

    var formData = new FormData(form)
    var object = {};
    formData.forEach(function(value, key){
        object[key] = value;
    });
    var json = JSON.stringify(object);
    console.log("here is the json I am posting", json)
    console.log(object)

    $.ajax('restaurant/make_booking/', {
        type: 'post',  // http method
        data: json,
        dataType: 'json',
        headers:{"X-CSRFToken": object.csrfmiddlewaretoken },
        contentType: "application/json; charset=utf-8",
        traditional: true,
        success: function (data, status, xhr) {

            swal({
                  title: "Booking Created!",
                  text: "Your booking reference is: " + data.booking_reference,
                  icon: "success",
                });

        },
        error: function (jqXhr, textStatus, errorMessage) {
            alert("failure")
            console.log(errorMessage)
        }
    });
}