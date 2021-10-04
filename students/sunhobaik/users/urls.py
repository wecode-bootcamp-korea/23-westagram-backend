from django.urls import path
from users.views import *
urlpatterns = [
    path('/sign', UserView.as_view()),
    path('/login', LoginView.as_view())
]