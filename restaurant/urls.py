# myapi/urls.py
from django.urls import include, path
from rest_framework import routers
from . import views

# router = routers.DefaultRouter()
# router.register(r'bookings', views.BookingsApiView, basename='bookings')

from django.views.i18n import JavaScriptCatalog

app_name="restaurant"

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:reservation_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:reservation_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('reservation/', views.reservation_page, name='add_reservation'),
    path('make_booking/' , views.MakeBooking.as_view()),
    path('cancel_booking' , views.CancelBooking.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('jsi18n', JavaScriptCatalog.as_view(), name='js-catlog')
]