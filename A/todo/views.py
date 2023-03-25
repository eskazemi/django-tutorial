from django.shortcuts import (
    render,
    redirect
)
from .models import Todo
from django.contrib import messages
from todo.forms import (
    TodoCreateForm,
    TodoUpdateForm,
)


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


def create(request):
    if request.method == 'POST':
        form = TodoCreateForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            Todo.objects.create(title=cd["title"], body=cd["body"])
            messages.success(request, "Created successfully", 'success')
            return redirect("all_todo")
    else:
        form = TodoCreateForm()
    return render(request, 'create.html', {'form': form})


def update(request, _id):
    todo = Todo.objects.get(id=_id)
    if request.method == 'POST':
        form = TodoUpdateForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            messages.success(request, "Update successfully", 'success')
            return redirect("detail", _id)
    else:
        form = TodoUpdateForm(instance=todo)
    return render(request, 'update.html', {'form': form})
