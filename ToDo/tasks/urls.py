from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePage, name='Home'),
    path('completed/', views.Completed, name='completed'),
    path('taskinfo/<int:task_id>/', views.TaskInfo, name='taskinfo'),
    path('createtask/', views.CreateTask, name='createtask'),
    path('edittask/<int:task_id>/', views.EditTask, name='edittask'),
    path('deletetask/<int:task_id>/', views.DeleteTask, name='deletetask')
]
