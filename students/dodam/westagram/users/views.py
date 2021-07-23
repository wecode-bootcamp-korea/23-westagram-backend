import json
from django.http import JsonResponse
from django.views import View
from users.models import User

# Create your views here.
class UserView(View):
	def post(self,request):
		data = json.loads (request.body)
		try:
			name = data['name']
			email = data['email']
			
