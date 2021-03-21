
from django.urls import path
from .views import ReservationView


urlpatterns = [
    path('booking', ReservationView.as_view())


]
