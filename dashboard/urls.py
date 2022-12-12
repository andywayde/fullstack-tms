from django.urls import path
from .views import ProjectList, ProjectCreate, ArchivedList, ProjectUpdate

urlpatterns = [
    path('', ProjectList.as_view(), name='dashboard'),
    path('/<int:pk>', ProjectUpdate.as_view(), name='project-details'),
    path('/new', ProjectCreate.as_view(), name='new-project'),
    path('/archived', ArchivedList.as_view(), name='archived'),
]
