from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm


def task_list(request):
    tasks = Task.objects.all().order_by('-created_at')
    return render(request, 'main/task_list.html', {'tasks': tasks})


def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'main/add_task.html', {'form': form})


def update_task(request, pk):
    task = get_object_or_404(Task, id=pk)
    form = TaskForm(request.POST or None, instance=task)
    if form.is_valid():
        form.save()
        return redirect('task_list')
    return render(request, 'main/update_task.html', {'form': form})


def complete_task(request, pk):
    task = get_object_or_404(Task, id=pk)
    task.completed = True
    task.save()
    return redirect('task_list')


def delete_task(request, pk):
    task = get_object_or_404(Task, id=pk)
    task.delete()
    return redirect('task_list')


from .models import Task, SubTask
from .forms import TaskForm, SubTaskForm


def add_subtask(request, pk):
    task = get_object_or_404(Task, id=pk)
    if request.method == 'POST':
        form = SubTaskForm(request.POST)
        if form.is_valid():
            subtask = form.save(commit=False)
            subtask.task = task
            subtask.save()
    return redirect('task_list')


def toggle_subtask(request, pk):
    subtask = get_object_or_404(SubTask, id=pk)
    subtask.completed = not subtask.completed
    subtask.save()
    return redirect('task_list')


def delete_subtask(request, pk):
    subtask = get_object_or_404(SubTask, id=pk)
    subtask.delete()
    return redirect('task_list')
