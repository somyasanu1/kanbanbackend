from django.urls import path

from dashboard.views import ViewTask, AddTask, DeleteTask, ViewAllTask

urlpatterns = [
    path('task/<int:pk>', ViewTask.as_view()),  # get and put
    path('tasks/', ViewAllTask.as_view()),  # get all
    path('task/add', AddTask.as_view()),  # post
    path('task/del/<int:pk>', DeleteTask.as_view()),  # delete
]
