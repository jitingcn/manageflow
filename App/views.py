from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def faqs(request):
    return HttpResponse("<h1> FAQ's </h1>")