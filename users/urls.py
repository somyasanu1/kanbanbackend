from django.urls import path
from .views import ViewUsers

urlpatterns = [
    # path('user/<int:pk>', ViewTask.as_view()),
    path('user/', ViewUsers.as_view()),
    path('user/<int:pk>', ViewUsers.as_view())
]
