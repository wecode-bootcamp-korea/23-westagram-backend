from django.urls import path

from users.views import UserView

urlpatterns = [
    path('/user_join', UserView.as_view()),
]