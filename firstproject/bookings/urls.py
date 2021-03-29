
from django.urls import path
from django.contrib import admin
from rest_framework import views
from .views import ReservationViewSet


urlpatterns = [
    path('admin/', admin.site.urls),
    path('reservation/', ReservationViewSet),


]
