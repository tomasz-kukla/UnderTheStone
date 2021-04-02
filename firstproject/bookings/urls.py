
from django.urls import path
from django.contrib import admin
from .views import ReservationViewSet


urlpatterns = [
    path('admin/', admin.site.urls),
    path('reservation/', ReservationViewSet),
    path('list/', ReservationViewSet.reservation_list),


]
