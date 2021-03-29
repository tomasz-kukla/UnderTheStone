
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from bookings.views import ReservationViewSet

router = DefaultRouter()
router.register('Reservation', ReservationViewSet)


urlpatterns = [
    path('api/', include('bookings.urls')),
]


for url in router.urls:
    print(url)
