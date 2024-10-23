from django.shortcuts import render
from todo.models import Todo
from todo.forms import TodoForm

def home_page(request):
    item_list = Todo.objects.order_by("-date")
    form = TodoForm(request.POST)
    dict_data = {
        'form' : form,
        'list' : item_list,
        'title' : "TODO LIST"
    }
    return render(request, 'todo/home.html', dict_data)

