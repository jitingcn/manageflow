from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import CreateNewList
from .models import ToDoList, Item
#from .filters import UserFilter

# Create your views here.
def board(request, id):
	ls = ToDoList.objects.get(id=id)
	return render(request, "board.html", {"ls":ls})

def index(request):
    return render(request, 'index.html')

def faqs(request):
    return HttpResponse("<h1> FAQ's </h1>")

def create(request):
    if request.method == 'POST':
        form = CreateNewList(request.POST)

        if form.is_valid():
            n= form.cleaned_data["name"]
            t = ToDoList(name=n)
            t.save()
            request.user.todolist.add(t)
            return HttpResponseRedirect("/%id" %t.id)
    else:
        form = CreateNewList()

    return render(request, "create.html", {"form":form})

@login_required(login_url="login")
def restricted(request):
    return HttpResponse("<h1> You are logged in </h1>")