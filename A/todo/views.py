from django.shortcuts import render
from django.http import HttpResponse
from .models import Todo

# Create your views here.
def sayhello(request):
    return render(request,'hello.html')
def all_todo(request):
    todos=Todo.objects.all()
    context={
        'todos':todos
    }
    return render(request,'todos.html',context) 

def detail(request,id):
    todo=Todo.objects.get(id=id)
    context={
        'todo':todo
    }
    return render(request,'detail.html',context)