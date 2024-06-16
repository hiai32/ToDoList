from django.shortcuts import render, redirect
from todolist.models import Task

# Create your views here.
def home(request, user_id):
    if request.method == 'POST':
        if 'update' in request.POST:
            task_id = request.POST['taskId']
            return redirect(update, user_id, task_id)
        elif 'delete' in request.POST:
            task_id = request.POST['taskId']
            task = Task.objects.get(pk=task_id)
            task.delete()

    context = {
        'user_id': user_id,
        'tasks': Task.objects.filter(userId=user_id)
    }

    return render(request, 'todolist/home.html', context)

def add(request, user_id):
    if request.method == 'POST':
        title = request.POST['title']
        due = request.POST['due']
        priority = request.POST['priority']
        explanation = request.POST['explanation']
        task = Task(title=title, due=due, priority=priority, explanation=explanation, userId=user_id)
        task.save()

        return redirect(home, user_id)
    
    context = {
        'user_id': user_id
    }

    return render(request, 'todolist/add.html', context)

def update(request, user_id, task_id):
    task = Task.objects.get(pk=task_id)
    if request.method == 'POST':
        task.title = request.POST['title']
        task.due = request.POST['due']
        task.priority = request.POST['priority']
        task.explanation = request.POST['explanation']
        task.save()

        return redirect(home, user_id)

    context = {
        'user_id': user_id,
        'task': task
    }

    return render(request, 'todolist/update.html', context)
