from django.urls import path
from .views      import UserView, UserLoginView

urlpatterns = [
    path("", UserView.as_view()),
    path("/login", UserLoginView.as_view()),
]
