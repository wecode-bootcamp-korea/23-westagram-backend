from django.urls import path
from users.views import User_View, User_LoginView

urlpatterns = [
    path('', User_View.as_view()),
    path('signup', User_LoginView.as_view()),
]
