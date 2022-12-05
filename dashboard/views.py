import time
from django.shortcuts import render, redirect

# Models
from .models import Project

# Forms
from .forms import ProjectForm
# Create your views here.

def getMonthTotal():
    current_month = time.strftime("%m")
    this_month_projects = Project.objects.filter(deadline__year='2022').filter(deadline__month=current_month)
    print(this_month_projects)
    sum = 0
    for project in this_month_projects:
        sum += project.total
    return sum

def dashboard(request):
    active_projects = Project.objects.filter(is_completed=False)
    month_total = getMonthTotal()

    context = {
        'active_projects': active_projects,
        'month_total': month_total,
    }

    return render(request, 'dashboard/index.html', context)

def new_project(request):
    if request.method == "GET":
        form = ProjectForm()
        context = {
            'form': form,
        }
        return render(request, 'dashboard/add_project.html', context)
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
