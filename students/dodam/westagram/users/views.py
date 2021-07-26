import json, re, jwt, bcrypt

from django.views import View
from django.http import JsonResponse

from users.models import User

password_regular = re.compile("^(?=.*[A-Za-z])(?=.*\d)(?=.*[$@$!%*#?&])[A-Za-z\d$@$!%*#?&]{8,}$")

class UserView(View):
	def post(self,request):
		try:	
			data = json.loads(request.body)  
			bcrypt_password = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

			if User.objects.filter(name=data['name']).exists() or User.objects.filter(email=data['email']).exists(): 			
				return JsonResponse({'MESSAGE': 'DATA_OVERLAP'}, status = 400)		

			if ('@' not in data['email']) or ('.'not in data['email']) or (not password_regular.match(data['password'])):
				return JsonResponse ({'MESSAGE': 'INVALID_FORMAT'}, status = 400)

			User.objects.create(
			name 		 = data['name'],
			email	 	 = data['email'],
			password	 = bcrypt_password,
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
			login_email = data['email']
			login_password = data['password'].encode('utf-8')

			if data['email'] == "" or data['password'] == "" :
				return JsonResponse ({'MESSAGE': 'WRONG_REQUEST'},status = 400)	

			db_email = User.objects.get(email=login_email)
			db_password = db_email.password.encode('utf-8')

			if not bcrypt.checkpw (login_password,db_password) :
				return JsonResponse ({'MESSAGE':'WRONG_PASSWORD'},status = 401)

			if not User.objects.filter(email=data['email']).exists():
				return JsonResponse ({'MESSAGE':'INVALID_USER'}, status =401)

			if data['password'] != User.objects.get(password=data['password']).password:
				return JsonResponse ({'MESSAGE':'INVALID_USER'}, status =401)
			return JsonResponse ({'MESSAGE':'SUCCESS'}, status = 200)

		except KeyError:
			return JsonResponse ({'MESSAGE':'KEY_ERROR'},status = 400)	
