import json, re

from django.views import View
from django.http import JsonResponse

from .models import User


class SignUp(View):
    def post(self, request):
        try:
            data = json.loads(request.body)

            if User.objects.filter(email=data['email']).exists():
                return JsonResponse({"message": "EMAIL_ALREADY_EXIST"}, status=400)

            if (data['email'] == '') or (data['password'] == ''):
                return JsonResponse({"message": "NO_INPUT"}, status=400)

            if re.match(r"^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", data['email']) is None:
                return JsonResponse({"message": "INVALID_FORMAT"}, status=400)

            if re.match(r"^(?=.*[A-Za-z])(?=.*\d)(?=.*[$@$!%*#?&])[A-Za-z\d$@$!%*#?&]{8,}$", data['password']) is None:
                return JsonResponse({"message": "INVALID_FORMAT"}, status=400)

            User.objects.create(
                name         =   data['name'],
                email        =   data['email'],
                password     =   data['password'],
                phone_number =   data['phone'],
                age          =   data['age']
            )

            return JsonResponse({"Message": "SUCCESS"}, status=201)
        
        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)

class SignIn(View):
    def post(self, request):
        try:
            data = json.loads(request.body)

            if (data['email'] == '') or (data['password'] == ''):
                return JsonResponse({"message": "KEY_ERROR"}, status=400)
            
            if not User.objects.filter(email=data['email']).exists():
                return JsonResponse({"message": "INVALID_USER"}, status=401)

            if data['password'] != User.objects.get(email=data['email']).password:
                return JsonResponse({"massage": "INVALID_USER"}, status=401)

            if User.objects.filter(email=data['email']) and User.objects.filter(password=data['password']):
                return JsonResponse({"message": "SUCCESS"}, status=200)

        except KeyError:
            return JsonResponse({"massage": "KEY_ERROR"}, status=400)