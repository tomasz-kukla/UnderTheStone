from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def main(request):
    return HttpResponse("<h1>Hello MAIN Page</h1>")


def about(request):
    return HttpResponse("<h1>Hello ABOUT Page</h1>")


def menu(request):
    return HttpResponse("<h1>Hello MENU Page</h1>")


def booking(request):
    return HttpResponse("<h1>Hello BOOKING Page</h1>")
