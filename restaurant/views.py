from django.http import HttpResponse


from django.http import HttpResponse

from .models import Reservation
from django.template import loader
from django.shortcuts import get_object_or_404, render


def index(request):
    latest_question_list = Reservation.objects.order_by('-time')[:5]
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

def vote(request, reservation_id):
    return HttpResponse("You're voting on reservation %s." % reservation_id)