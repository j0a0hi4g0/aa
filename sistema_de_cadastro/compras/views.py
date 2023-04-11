from django.shortcuts import render
from django.http import HttpResponse 
from .models import compras, Airport
def index(request):
    return render(request, "flights/index.html", {
        "compras": compras.objects.all()
    })
