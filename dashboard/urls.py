from django.urls import path
from .views import dashboard, new_project, archived, project_details

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('/<int:id>', project_details, name='project-details'),
    path('/new', new_project, name='new-project'),
    path('/archived', archived, name='archived'),
]
