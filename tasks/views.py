from ctypes.wintypes import tagMSG
from django.shortcuts import render
from tasks.models import Task
from django.views.decorators.csrf import csrf_protect, csrf_exempt


def home(request):
    template_name = 'home.html'

    return render(request, template_name, context=None)


def search(request):
    template_name = 'home.html'
    all_tasks = Task.objects.all()
    if request.method == 'POST':
        tasks = request.POST.get('search')
        searched_task = Task.objects.filter(title__icontains=tasks)
        print(searched_task)

        context = {
            'tasks': searched_task,
        }
        return render(request, template_name, context=context)
    else:
        context = {
            'all_tasks': all_tasks
        }
        return render(request, template_name, context=None)
    

def tag_list(request, tag):
    template_name = 'tag_list.html'
    tasks = Task.objects.filter(tags=tag)
    
    context = {
        'tasks': tasks
    }
    return render(request, template_name, context=context)

def tags(request):
    template_name = 'tags.html'
    tasks = Task.objects.all()
    
    context = {
        'tasks': tasks
    }
    return render(request, template_name, context=context)