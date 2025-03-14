from django.urls import path
from . import views

app_name = "todoapp"

urlpatterns = [
    path('',views.home,name="home"),
    path('task-detail/<int:id>/',views.task_detail,name="task_detail"),
    path('add_task/',views.add_task,name="add_task"),
    path('task-update/<int:id>',views.task_edit,name="task_update"),
    path('task-delete/<int:id>/',views.task_delete,name="task_delete"),
]