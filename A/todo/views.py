from django.shortcuts import (
    render,
    redirect
)
from .models import Todo
from django.contrib import messages


def get_all(request):
    todos = Todo.objects.all()
    context = {
        'todos': todos
    }
    return render(request, 'todos.html', context)


def detail(request, _id: int):
    todo = Todo.objects.get(id=_id)
    context = {
        'todo': todo
    }
    return render(request, 'detail.html', context)


def delete(request, _id: int):
    Todo.objects.filter(id=_id).delete()
    messages.success(request, "Delete Message successfully", 'success')
    return redirect("all_todo")
