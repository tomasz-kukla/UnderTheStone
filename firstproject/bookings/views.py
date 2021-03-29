
from rest_framework import viewsets
from django.db.models import fields, query
from django.shortcuts import render
from rest_framework import generics
from rest_framework import serializers
from rest_framework.decorators import action
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from .serializers import ReservationSerializer
from .models import Reservation
from rest_framework.response import Response
from rest_framework import status, generics


class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer()
