from django.shortcuts import render, redirect
from todolist.models import Task

# Create your views here.
def home(request):
    if request.method == 'POST':
        id = request.POST['id']
        task = Task.objects.get(pk=id)
        task.delete()

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
