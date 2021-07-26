import json, re

from django.views import View
from django.http import JsonResponse

from users.models import User

password_regular = re.compile("^(?=.*[A-Za-z])(?=.*\d)(?=.*[$@$!%*#?&])[A-Za-z\d$@$!%*#?&]{8,}$")

class UserView(View):
	def post(self,request):
		try:	
			data = json.loads(request.body)  
			if User.objects.filter(name=data['name']).exists() or User.objects.filter(email=data['email']).exists(): 			
				return JsonResponse({'MESSAGE': 'DATA_OVERLAP'}, status = 400)		

			if ('@' not in data['email']) or ('.'not in data['email']) or (not password_regular.match(data['password'])):
				return JsonResponse ({'MESSAGE': 'INVALID_FORMAT'}, status = 400)

			User.objects.create(
			name 		 = data['name'],
			email	 	 = data['email'],
			password	 = data['password'],
			phone_number = data['phone_number'], 
			birthday 	 = data['birthday'],
			)
			return JsonResponse ({'MESSAGE':'SUCCESS'}, status = 201)

		except KeyError: 
			return JsonResponse ({'MESSAGE':'KEY_ERROR'}, status = 400)

class LoginView(View):
	def post(self,requset):
		try:
			data = json.loads(requset.body)

			if data['email'] =="" or data['password'] == "" :
				return JsonResponse ({'MESSAGE': 'WRONG_REQUEST'},status = 400)	

			if not User.objects.filter(email=data['email']).exists():
				return JsonResponse ({'MESSAGE':'INVALID_USER'}, status =401)

			if data['password'] != User.objects.get(password=data['password']).password:
				return JsonResponse ({'MESSAGE':'INVALID_USER'}, status =401)
			return JsonResponse ({'MESSAGE':'SUCCESS'}, status = 200)

		except KeyError:
			return JsonResponse ({'MESSAGE':'KEY_ERROR'},status = 400)	