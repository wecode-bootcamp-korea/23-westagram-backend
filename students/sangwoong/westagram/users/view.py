from django.shortcuts import render


import json

from django.http  import JsonResponse 
from django.views import View

from .models	  import User


class UserView(View):
    def post(self,request):
        try:
            data = json.loads(request.body)
            
            MINIMUM_PASSWORD_LENGTH = 8
            if '@' not in data['email'] or '.' not in data['email']:
                return JsonResponse({'MESSAGE' : 'INVALID EMAIL'}, status=400)

            if len(data['password']) < MINIMUM_PASSWORD_LENGTH:
                return JsonResponse({'MESSAGE' : 'INVALID PASSWORD'}, status=400)

            if User.objects.filter(email=data['email']).exists():
                return JsonResponse({'MESSAGE' : 'DUPLICATED EMAIL'}, status=400)

            if User.objects.filter(phone_number=data['phone_number']).exists():
                return JsonResponse({'MESSAGE' : 'DUPLICATED PHONE_NUM'}, status=400)

            if User.objects.filter(name=data['name']).exists():
                return JsonResponse({'MESSAGE' : 'DUPLICATED NAME'}, status=400)

              
            User.objects.create(
                name         = data['name'],
                phone_number = data['phone_number'],
                password     = data['password'],
                email         = data['email']
            )
            return JsonResponse({'MESSAGE' : 'SUCCESS'}, status=201)  #성공하면 석세스 메세지 날림.
        except KeyError:
            return JsonResponse({'MESSAGE' : 'KEY ERROR'}, status=400)

class SigninView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            password     = data['password']
            email        = data['email']

            if data['email']=="" or data['password']=="":
                return JsonResponse({"MESSAGE":"NOT_FOUND"},status=404)
            
            if not User.objects.filter(email=data['email']).exists():
                return JsonResponse({"MESSAGE" : "INVALID_USER"}, status=401)
                
            if User.objects.get(email=data['email']).password !=data['password']:
                return JsonResponse({"MESSAGE" : "INVALID_USER"}, status=401)

        except KeyError:
            return JsonResponse({"MESSAGE" : "KEY_ERROR"}, status=400)
            return JsonResponse({"MESSAGE":"SUCCESS"}, status=200)
