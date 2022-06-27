from django.http import HttpResponse


from django.http import HttpResponse, HttpResponseRedirect

from .models import Reservation, Restaurant
from django.template import loader
from django.shortcuts import get_object_or_404, render
from datetime import datetime
from django.urls import reverse

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
    restaurant = Restaurant.objects.first()
    no_of_tables = Restaurant.no_of_tables
    reservations = Reservations.objects.all()

    current_year = timezone.now().day
    current_day = timezone.now().day
    # double booking
    if Reservation.objects.filter(time__day=current_day, time__hour=current_hour).count() > no_of_tables:
        return render(request, 'restaurant/index.html', {
            'error_message': "You didn't select a choice.",
        })

    reservation = Reservation.objects.create(name=name, email=email,time=datetime.now(), restaurant=restaurant)
    
    return HttpResponseRedirect(reverse('restaurant:index'))
    