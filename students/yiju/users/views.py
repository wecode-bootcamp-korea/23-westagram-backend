import json
import re
import bcrypt, jwt

from django.http  import JsonResponse
from django.views import View

from users.models import User
from my_settings import SECRET_KEY

class UserView(View):
	def post(self, request):
		try: 
			data     = json.loads(request.body)
			email    = data['email']
			password = data['password']

			email_regx    = r'[\w\.-]{3,15}@[\w\.-]{2,}\.\w{2,4}\b'
			password_regx = r'^(?=(.*[A-Za-z]))(?=(.*[0-9]))(?=(.*[@#$%^!&+=.\-_*]))([a-zA-Z0-9@#$%^!&+=*.\-_]){8,}$'

			email_val     = re.match(email_regx, email)
			password_val  = re.match(password_regx, password)

			if not email_val:
				return JsonResponse({'message':'wrong_email'}, status=400)

			if not password_val:
				return JsonResponse({'message':'wrong_pasword'}, status=400)

			if User.objects.filter(email=email).exists():
				return JsonResponse({'message':'email_already_exists'}, status=400)

			hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

			User.objects.create(
				name     = data['name'],
				email    = email,
				password = hashed_password.decode('utf-8'),
				contact  = data['contact']
				)	
			return JsonResponse({'message':'success'}, status=201)

		except KeyError:
			return JsonResponse({'message':'key_error'}, status=400)

		

class LoginView(View):
	def post(self,request):
		try:
			data     = json.loads(request.body)
			email    = data['email']
			password = data['password']
			user     = User.objects.get(email=email)

			if not User.objects.filter(email=email).exists():
				return JsonResponse({'message':'INVALID_USER'}, status=401)

			if not bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
				return JsonResponse({'message':'INVALID_USER'}, status=401)
			
			SECRET = SECRET_KEY
			token  = jwt.encode({'id' : user.id }, SECRET, algorithm = 'HS256')

			return JsonResponse({'access_token': token }, status = 200)

		except KeyError:
			return JsonResponse({'message':'KEY_ERROR'}, status=400)