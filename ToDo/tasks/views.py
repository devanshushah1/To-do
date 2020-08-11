from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

# Create your views here.


def HomePage(request):
    tasks = Task.objects.filter(status="Pending")
    context = {'tasks': tasks}
    return render(request, 'tasks/index.html', context)


def Completed(request):
    tasks = Task.objects.filter(status="Completed")
    context = {'tasks': tasks}
    return render(request, 'tasks/completed.html', context)


def TaskInfo(request, task_id):
    task = Task.objects.get(id=task_id)
    context = {'task': task}
    return render(request, 'tasks/taskinfo.html', context)


def CreateTask(request):
    form = TaskForm()
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            priority = form.cleaned_data['priority']
            status = form.cleaned_data['status']
            Task.objects.create(name=name, description=description, priority=priority, status=status)
            return redirect('/')

    context = {'form': form}
    return render(request, 'tasks/taskform.html', context)


def EditTask(request, task_id):
    task = Task.objects.get(id=task_id)
    form = TaskForm(instance=task)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'tasks/taskform.html', context)


def DeleteTask(request, task_id):
    task = Task.objects.get(id=task_id)
    if request.method == "POST":
        task.delete()
        return redirect('/')

    context = {'task': task}
    return render(request, 'tasks/deletetask.html', context)
