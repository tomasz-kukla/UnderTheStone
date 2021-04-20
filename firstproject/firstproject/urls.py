
from django.urls import path, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter

from bookings.views import ReservationViewSet

router = DefaultRouter()
router.register('Reservations', ReservationViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include((router.urls, 'Reservations'), namespace='Reservations')),
]


for url in router.urls:
    print(url)
