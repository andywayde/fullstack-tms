import time
from django.urls import reverse_lazy

# Class-based views
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView
from django.views.generic import CreateView

# Login view
from django.contrib.auth.views import LoginView

# Mixins
from django.contrib.auth.mixins import LoginRequiredMixin

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

class CustomLoginView(LoginView):
    template_name = 'dashboard/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('dashboard')

class ProjectList(LoginRequiredMixin, ListView):
    model = Project
    context_object_name = 'active_projects'
    template_name = 'dashboard/index.html'
    queryset = Project.objects.filter(is_completed=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        month_total = getMonthTotal()
        context["month_total"] = month_total
        return context
    

class ProjectUpdate(LoginRequiredMixin, UpdateView):
    model = Project
    fields = '__all__'
    template_name = 'dashboard/project_details.html'
    success_url = reverse_lazy('dashboard')

class ProjectCreate(LoginRequiredMixin, CreateView):
    model = Project
    template_name = 'dashboard/add_project.html'    
    success_url = reverse_lazy('dashboard')
    form_class = ProjectForm

class ArchivedList(LoginRequiredMixin, ListView):
    model = Project
    queryset = Project.objects.filter(is_completed=True)
    context_object_name = 'completed_projects'
    template_name = 'dashboard/archived.html'
