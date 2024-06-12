from django.shortcuts import render, redirect
from todolist.models import Task

# Create your views here.
def home(request):
    if request.method == 'POST':
        if 'delete' in request.POST:
            id = request.POST['id']
            task = Task.objects.get(pk=id)
            task.delete()
        elif 'update' in request.POST:
            id = request.POST['id']
            return redirect(update, id)

    context = {
        'tasks': Task.objects.all()
    }

    return render(request, 'todolist/home.html', context)

def add(request):
    if request.method == 'POST':
        title = request.POST['title']
        due = request.POST['due']
        priority = request.POST['priority']
        explanation = request.POST['explanation']
        task = Task(title=title, due=due, priority=priority, explanation=explanation)
        task.save()

        return redirect(home)

    return render(request, 'todolist/add.html')

def update(request, id):
    task = Task.objects.get(pk=id)
    if request.method == 'POST':
        task.title = request.POST['title']
        task.due = request.POST['due']
        task.priority = request.POST['priority']
        task.explanation = request.POST['explanation']
        task.save()

        return redirect(home)

    context = {
        'task': task
    }

    return render(request, 'todolist/update.html', context)
