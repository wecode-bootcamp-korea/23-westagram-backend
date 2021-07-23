from django.urls import path
from users.views import User_View, User_LoginView

urlpatterns = [
    path('create', User_View.as_view()),
    path('login', User_LoginView.as_view()),
]
