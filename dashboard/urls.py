from django.urls import path
from .views import dashboard, new_project

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('/new', new_project, name='new-project'),
]
