import json
import re

from django.http  import JsonResponse
from django.views import View

from users.models import User

class UserView(View):
    def post(self,request):
        try:
            data = json.loads(request.body)

            email_validation    = re.compile('\w+[@]\w+[.]\w+')
            password_validation = re.compile('\S{8,}')

            if not email_validation.match(data['email']):
                return JsonResponse({"message":"INVALID_EMAIL_FORMAT"}, status=400)

            if not password_validation.match(data['password']):
                return JsonResponse({"message":"PASSWORD_TOO_SHORT"}, status=400)

            if User.objects.filter(email=data['email']).exists():
                return JsonResponse({"message":'EMAIL_ALREADY_EXISTS'}, status=400)

            User.objects.create(
                name         = data['name'],
                email        = data['email'],
                password     = data['password'],
                phone_number = data['phone_number'],
                age          = data['age'],
            )

            return JsonResponse({"message":"SUCCESS"}, status=201)

        except KeyError:
            return JsonResponse({"message":"KEY_ERROR"}, status=400)

class LoginView(View):
    def post(self,request):
        try:
            data = json.loads(request.body)

            if not User.objects.filter(email=data['email']).exists():
                return JsonResponse({"message":"INVALID_USER"}, status=401)
            
            if data['password'] != User.objects.get(email=data['email']).password:
                return JsonResponse({"message":"INVALID_USER"}, status=401)
            
            return JsonResponse({"message":"SUCCESS"}, status=200)

        except KeyError:
            return JsonResponse({"message":"KEY_ERROR"}, status=400)
        
        
            
