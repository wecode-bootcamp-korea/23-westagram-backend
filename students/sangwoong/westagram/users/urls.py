from django.urls import path
from users.view import UserView

urlpatterns = [ 
	path ('', UserView.as_view())
] 
