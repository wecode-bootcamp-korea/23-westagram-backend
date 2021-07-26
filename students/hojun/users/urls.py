from django.urls import path
from users.views import UserView, LogInView

urlpatterns = [
    path('/signup', UserView.as_view()),
    path('/login', LogInView.as_view())
]
