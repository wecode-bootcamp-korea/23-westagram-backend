import json
import re

from django.http import JsonResponse
from django.views import View

from users.models import User

class UserView(View):
    def post(self, request):
        try:
            data         = json.loads(request.body)
            name         = data['name']
            email        = data['email']
            password     = data['password']
            phone_number = data['phone_number']
            age          = data['age']

            password_validation = re.compile('\s')
            email_validation = re.compile('[\w]+@[\w]+[.]+[\w]+')
            if (password_validation.search(password) is not None) or (len(password) < 8) or email_validation.match(email) is None:
                return JsonResponse({'MESSAGE' : 'INVALID_FORMAT'}, status = 400)

            if User.objects.filter(email=email).exists():
                return JsonResponse({'MESSAGE' : "ALREADY_EXISTS"}, status = 400)

            User.objects.create(
                name         = name,
                email        = email,
                password     = password,
                phone_number = phone_number,
                age          = age
            )
            return JsonResponse({'MESSAGE' : "SUCCESS"}, status=201)    

        except KeyError:
            return JsonResponse({'MESSAGE' : 'KEY_ERROR'}, status = 400)


class LogInView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            email = data['email']
            password = data['password']

            if not User.objects.filter(email=email).exists():
                return JsonResponse({"MESSAGE" : "INVALID_USER"}, status=401)
            
            if User.objects.get(email=email).password != password:
                return JsonResponse({"MESSAGE" : "SUCCESS"}, status=200)


        except KeyError:
            return JsonResponse({'MESSAGE' : 'KEY_ERROR'}, status=400)