from django.urls import path
from users.views import *

urlpatterns = [
    path('create_user', User_CreateView.as_view()),
]
