from django.shortcuts import render, redirect
from .models import Todolist
from .forms import TodoItem

from django.views.decorators.http import require_POST
# Create your views here.

def index(request):
    list_items=Todolist.objects.order_by('id')
    form = TodoItem()
    context={'list_items':list_items, 'form':form}
    return render(request, 'todolist/index.html', context)

@require_POST
def addItem(request):
    form = TodoItem(request.POST)
    if form.is_valid():
        new_todo = Todolist(text=request.POST['text'])
        new_todo.save()
    return redirect('index')

def completedTodo(request, todo_id):
    todo = Todolist.objects.get(pk=todo_id)
    todo.completed = True
    todo.save()
    return redirect('index')

def deleteCompleted(request):
    Todolist.objects.filter(completed__exact=True).delete()
    return redirect('index')

def deleteAll(request):
    Todolist.objects.all().delete()
    return redirect('index')
