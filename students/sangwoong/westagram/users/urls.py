from django.urls import path
from users.view import UserView, SigninView

urlpatterns = [ 
	path ('signup', UserView.as_view()),
	path ('signin', SigninView.as_view())
] 
