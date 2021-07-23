from django.urls import path
from users.views import User_View

urlpatterns = [
    path('', User_View.as_view()),
]
