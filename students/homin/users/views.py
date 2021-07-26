import json
import re

from django.views import View
from django.http  import JsonResponse

from users.models import User

class UserView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)

            if not re.match('^\w+@\w+\.\w+$', data['email']):
                return JsonResponse({"message": 'INVALID_EMAIL_FORMAT'}, status=400)

            if (not re.match('\S{1,8}', data['password']) or
                    len(data['password']) < 8):
                return JsonResponse({"message": 'INVALID_PASSWORD_FORMAT'}, status=400)

            if not re.match('\d{3}-\d{3,4}-\d{4}', data['phone_number']):
                return JsonResponse({"message": 'INVALID_PHONE_NUMBER_FORMAT'}, status=400)

            if User.objects.filter(email=data['email']).exists():
                return JsonResponse({"message": 'EXISTED_EMAIL'}, status=400)

            User.objects.create(
                name         = data['name'],
                email        = data['email'],
                password     = data['password'],
                phone_number = data['phone_number']
            )
            return JsonResponse({"message": "SUCCESS"}, status=201)

        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)
        
        except Exception:
            return JsonResponse({"message": "INVALID_VALUE"}, status=400)

class SigninView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)

            if not User.objects.filter(email=data['email'], password=data['password']).exists:
                return JsonResponse({"message": "INVALID_USER"}, status=401)
            
            User(name=data['email'], password=data['password'])
            return JsonResponse({"message": "SUCCESS"}, status=200)
        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)
