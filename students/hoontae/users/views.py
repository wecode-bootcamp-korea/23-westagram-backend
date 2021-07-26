import json, bcrypt

from django.http       import JsonResponse
from django.views      import View

from users.models      import User
from users.validations import email_validation, password_validation

class SignupView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            password     = data['password']
            hashed_password = bcrypt.hashpw(password.encode('utf-8'),bcrypt.gensalt()).decode('utf-8')

            if not email_validation(data['email']):
                return JsonResponse({'message':'INVALID_EMAIL_FORMAT'}, status=400)
            
            if not password_validation(data['password']):
                return JsonResponse({'message':'CHARACTER_SHORT'}, status=400)

            if User.objects.filter(email=data['email']).exists():
                return JsonResponse({'massage':'INVALID_EMAIL'}, status=400)
            

            User.objects.create(
                name         = data['name'],
                email        = data['email'],
                password     = hashed_password,
                phone_number = data['phone_number'],
                birthday     = data['birthday'],
            )
            return JsonResponse({'message':'SUCCESS'}, status=201)
        except KeyError:
            return JsonResponse({'message':'KEY_ERROR'}, status=400)

class LoginView(View):
    def post(self, request):
        try: 
            data = json.loads(request.body)

            if not User.objects.filter(email=data['email']).exists():
                return JsonResponse({'message':'INVALID_USER'}, status=401)

            if not bcrypt.checkpw(data['password'].encode('utf-8'), User.objects.get(email = data['email']).password.encode('utf-8')):
                return JsonResponse({'message':'INVALID_USER'}, status=401)

            return JsonResponse({'message':'SUCCESS'}, status=200)
        except KeyError:
            return JsonResponse({'message':'KEY_ERROR'}, status=400)