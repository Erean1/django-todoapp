from django.shortcuts import render,get_object_or_404,redirect
from .forms import TaskForm
from .models import Task
from django.contrib.auth.decorators import login_required

def home(request):
    if not request.user.is_authenticated:
        return redirect("users:login")
    
    task = Task.objects.filter(author=request.user)
    return render(request,'todoapp/home.html',{'tasks' : task})


def task_detail(request,id):
    task = get_object_or_404(Task,id=id)
    return render(request,'todoapp/task_detail.html',{'task' : task})

@login_required(login_url="users:login")
def add_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.author = request.user
            task.save()
            return redirect('todoapp:home')
    else:
        form = TaskForm()

    return render(request,'todoapp/add_task.html',{'form' : form})


def task_edit(request,id):
    task = get_object_or_404(Task,id=id)
    if request.user != task.author:
        return redirect('todoapp:home')
    if request.method == "POST":
        form = TaskForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
            return redirect('todoapp:task_detail',id=task.id)
    else:
        form = TaskForm(instance=task)
    return render(request,'todoapp/task_update.html',{'form' : form})



def task_delete(request,id):
    task = get_object_or_404(Task,id=id)

    if request.user != task.author and  not request.user.is_superuser:
        return redirect('todoapp:home')

    if request.method == "POST":
        task.delete()
        return redirect('todoapp:home')

    return render(request,'todoapp/confirm_delete.html',{'task' : task})


