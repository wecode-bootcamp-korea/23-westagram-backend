from django.urls import path, include
from users.views import UserView, LoginView
urlpatterns = [
    path('', UserView.as_view()),
    path('/login', LoginView.as_view())
]