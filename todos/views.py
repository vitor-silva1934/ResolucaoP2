from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from .models import Todo
from datetime import date
from django.shortcuts import get_object_or_404, redirect


def home(request):
    return render(request, "home.html")


class TodoListView(ListView):
    model=Todo


class TodoCreateView(CreateView):
    model=Todo
    fields=["title","deadline"]
    success_url=reverse_lazy("todo_list")


# Create your views here.
