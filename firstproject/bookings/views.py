from django.db.models import query
from django.shortcuts import render
from rest_framework import generics
from .serializers import ReservationSerializer
from .models import Reservation

# create all tables view


class ReservationView(generics.ListAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
