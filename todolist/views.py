import math
from django.shortcuts import render, redirect
from django.db.models import Q
from todolist.models import Task
from account.models import User

# Create your views here.
def home(request, user_id):
    if request.method == 'POST':
        task_id = request.POST['taskId']
        if 'achieve' in request.POST:
            task = Task.objects.get(pk=task_id)
            task.isAchieved = 1
            task.save()
            user = User.objects.get(pk=user_id)
            user.achievedTasks += 1
            user.save()
        elif 'update' in request.POST:
            return redirect(update, user_id, task_id)
        elif 'delete' in request.POST:
            task = Task.objects.get(pk=task_id)
            task.delete()

    context = {
        'userId': user_id,
        'tasks': Task.objects.filter(userId=user_id, isAchieved=0),
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

        user = User.objects.get(pk=user_id)
        user.addedTasks += 1
        user.save()

        return redirect(home, user_id)
    
    context = {
        'userId': user_id,
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
        'userId': user_id,
        'task': task,
    }

    return render(request, 'todolist/update.html', context)

def mypage(request, user_id):
    user = User.objects.get(pk=user_id)
    
    factorial = 1
    level = 1
    while factorial <= user.achievedTasks:
        level += 1
        factorial = math.factorial(level)


    if user.addedTasks == 0:
        achievementRate = 0
    else:
        achievementRate = user.achievedTasks / user.addedTasks * 100

    context = {
        'user': user,
        'level': level,
        'achievementRate': round(achievementRate, 1),
        'tasks': Task.objects.filter(userId=user_id, isAchieved=1).order_by('-id'),
    }
    
    return render(request, 'todolist/mypage.html', context)

def search(request, user_id):
    if request.method == 'POST':
        keyword = request.POST['search']
        tasks = Task.objects.filter(Q(title__icontains=keyword) | Q(explanation__icontains=keyword))

    context = {
        'userId': user_id,
        'tasks': tasks,
    }

    return render(request, 'todolist/search.html', context)
