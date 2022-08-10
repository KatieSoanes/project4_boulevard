from django.urls import path

from . import views

app_name="restaurant"

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:reservation_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:reservation_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('add_reservation/', views.add_reservation, name='add_reservation'),
    path('make_booking/' , views.MakeBooking.as_view())
]