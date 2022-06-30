from django.http import HttpResponse
from django.shortcuts import render


def request_handler(request):
    context = {"branavName": "sus"}
    return render(request, "index.html", context)


def amogus_handler(request):
    context = {}
    return render(request, "amogus.html", context)
