from django.shortcuts import render
from .models import Todolist
# Create your views here.

def index(request):
    list_items=Todolist.objects.order_by('id')
    context={'list_items':list_items}
    return render(request, 'todolist/index.html', context)
