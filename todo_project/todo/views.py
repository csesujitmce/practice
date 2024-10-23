from django.shortcuts import render, redirect
from todo.models import Todo
from todo.forms import TodoForm
from django.contrib import messages

def home_page(request):
    item_list = Todo.objects.order_by("-date")
    status = False
    # form = TodoForm()
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            status = True
    form = TodoForm()
    dict_data = {
        'form' : form,
        'lists' : item_list,
        'title' : "TODO LIST",
        'status' : status,
    }
    return render(request, 'todo/home.html', dict_data)

def delete_todo_item(request, id):
    item = Todo.objects.get(id=id)
    item.delete()
    messages.info(request, "Notes deteted!!!")
    return redirect('home')
