from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request):
    return render(request, "index.html")

def contact(request):
    return render(request, "contact.html")