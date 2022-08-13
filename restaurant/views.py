from django.http import HttpResponse


from django.http import HttpResponse, HttpResponseRedirect

from .models import Reservation, Restaurant, Booking
from .serializers import BookingSerializer
from .BookingCalendar import BookingCalendar
from rest_framework import status
from rest_framework import permissions
from rest_framework.response import Response
from django.contrib.admin.widgets import AdminDateWidget
from django import forms
from django.template import loader
from django.shortcuts import get_object_or_404, render
from datetime import datetime
from django.urls import reverse
from django.utils import timezone

from rest_framework.views import APIView

import datetime
import calendar

def get_bookings_for_month(month):
    dateMaxMin = calendar.monthrange(2022, month)
    dateMax = dateMaxMin[1]

    start_date = datetime.date(2022, month, 1)
    end_date = datetime.date(2022, month, dateMax)


    return Booking.objects.filter(date__range=(start_date, end_date))

def get_booking_by_reference(reference):
    return Booking.objects.filter(booking_reference = reference)



def get_booking_calendar(month):
    bookings_for_month = get_bookings_for_month(month)
    serializer = BookingSerializer(bookings_for_month, many=True)
    booking_calendar = BookingCalendar(month)
    booking_calendar.hydrate_bookings(serializer.data)
    return booking_calendar

def index(request):
    latest_question_list = Reservation.objects.order_by('-time')
    template = loader.get_template('restaurant/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, reservation_id):
    reservation = get_object_or_404(Reservation, pk=reservation_id)
    return render(request, 'restaurant/detail.html', {'reservation': reservation})

def results(request, reservation_id):
    response = "You're looking at the results of reservation %s."
    return HttpResponse(response % reservation_id)

def add_reservation(request):
    name = request.POST['name']
    email = request.POST['email']
    date = request.POST['date']
    restaurant = Restaurant.objects.first()
    no_of_tables = Restaurant.no_of_tables
    reservations = Reservation.objects.all()

    current_day = timezone.now().day
    current_hour = timezone.now().hour
    # double booking
    
    if Reservation.objects.filter(time__day=current_day, time__hour=current_hour).count() > restaurant.no_of_tables:
        return render(request, 'restaurant/index.html', {
            'error_message': "You didn't select a choice.",
        })

    reservation = Reservation.objects.create(name=name, email=email,time=datetime.now(), restaurant=restaurant)
    
    return HttpResponseRedirect(reverse('restaurant:index'))

class MakeBooking(APIView):

    def post(self, request):
        year, month, day = request.data["date"].split("-")
        month= int(month)
        day = str(int(day))
        date = datetime.date(2022, month, int(day))
        get_booking_calendar(month)

        group_size = int(request.data["groupSize"])

        booking_calendar = get_booking_calendar(month)
        booking_response = booking_calendar.make_booking_for_day(day, group_size)

        if (booking_response["response"] == 200):
            data_to_save = {
                "date": date,
                'booking_reference': str(booking_response["booking_reference"]),
                "num_guests": group_size
            }
            print(f"cheff made it here")
            serializer = BookingSerializer(data=data_to_save)
            if serializer.is_valid():
                serializer.save()
                # return  render(request, "booking-success.html", context=serializer.data)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(booking_response,status=status.HTTP_400_BAD_REQUEST)

class CancelBooking(APIView):

    def post(self, request):
        booking_reference = request.data["booking_reference"]
        query_set = get_booking_by_reference(booking_reference)
        serializer = BookingSerializer(query_set, many=True)
        row_to_delete = dict(serializer.data[0])
        year, month, day = row_to_delete["date"].split("-")
        day = str(int(day))
        month = int(month)
        get_booking_calendar(month)
        booking_calendar = get_booking_calendar(month)

        booking_response = booking_calendar.cancel_booking_for_day(day, booking_reference)
        if (booking_response["response"] == 200):
            booking_to_delete = get_booking_by_reference(booking_reference)
            booking_to_delete.delete()
            return Response(booking_response, status=status.HTTP_201_CREATED)
        else:
            return Response(booking_response,status=status.HTTP_400_BAD_REQUEST)

class DateForm(forms.Form):
    date = forms.DateField(widget=AdminDateWidget(attrs={'type': 'date'}))
    groupSize = forms.IntegerField()

class CancelBookingForm(forms.Form):
    booking_reference = forms.CharField(max_length=255)


def reservation_page(request):
    return render(request, "reservations.html", context={ "form": DateForm(), "cancel_form" : CancelBookingForm(), "value":[2,4,6,8]})