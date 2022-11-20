from django.shortcuts import render
from .models import Project

import datetime

# Create your views here.


def sum_calculation(projects):
    sum = 0
    for project in projects:
        sum += project.total
    return sum


def index(request):
    # get current month
    today = datetime.date.today()
    this_month = today.month
    # get active projects
    active_projects = Project.objects.filter(is_completed=False)
    # get this month's projects
    month_projects = Project.objects.filter(deadline__month=this_month)

    print(month_projects)

    total_this_month = sum_calculation(month_projects)
    context = {
        'active_projects': active_projects,
        'total_this_month': total_this_month,
        'month': today.strftime("%B"),
        'day': today.day,
    }
    return render(request, "my_tms/dashboard.html", context)
