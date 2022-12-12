from django.urls import path
from .views import ProjectList, ProjectCreate, ArchivedList, ProjectUpdate, CustomLoginView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),

    path('dashboard/', ProjectList.as_view(), name='dashboard'),
    path('dashboard/<int:pk>/', ProjectUpdate.as_view(), name='project-details'),
    path('dashboard/new/', ProjectCreate.as_view(), name='new-project'),
    path('dashboard/archived/', ArchivedList.as_view(), name='archived'),
]
