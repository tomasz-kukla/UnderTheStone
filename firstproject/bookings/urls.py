
from django.urls import path
from .views import main, about, menu, booking


urlpatterns = [
    path('home', main),
    path('', main),
    path('about', about),
    path('menu', menu),
    path('booking', booking)


]
