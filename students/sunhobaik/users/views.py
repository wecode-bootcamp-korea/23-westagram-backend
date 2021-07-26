from django.http.response import JsonResponse
from django.views import View
import json
from users.models import User
import re

class UserView(View):
    def post(self, request):
        try:
            data  = json.loads(request.body)
            Email = re.compile("^[a-zA-Z0-9+-_.]+@[a-zA-z0-9-]+\.[a-zA-z0-9-]+$")
            PW    = re.compile("/^(?=.*[a-zA-Z])((?=.*\d)|(?=.*\W)).{8,20}$/")
       
            if  PW.match(data['password'])  is None or Email.match(data['email']) is None:
                return JsonResponse({'message':' INVALID_FORMAT'}, status=400)         
            
            if User.objects.filter(email = data["email"]).exists():
                return JsonResponse({"message": "OVERLAP"}, status=400)

            User.objects.create(
                name          = data['name'],
                email         = data['email'],
                password      = data['password'],
                phone_numbers = data['phone_numbers'],
                web_site      = data['website'],
                nick_name     = data['nick_name'],
                address       = data['address'],
                introduce     = data['introduce']
            )           
            return JsonResponse({'message': "SUCCESS"}, status=201)

        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)


class LoginView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            
            if not User.objects.filter(email=data['email']).exists():
                return JsonResponse({"message": "INVALID_USER"}, status=401)
            
            if User.objects.get(email=data['email']).password != data['password']:
                return JsonResponse({"message": "INVALID_USER"}, status=401)
                    
            return JsonResponse({'message': "SUCCESS"}, status=200)
        
        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)


