import json
import re
import bcrypt
import jwt

from django.views import View
from django.http  import JsonResponse

from my_settings import SECRET_KEY
from users.models import User

class UserView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)

            if not re.match('^\w+@\w+\.\w+$', data['email']):
                return JsonResponse({"message": 'INVALID_EMAIL_FORMAT'}, status=400)

            if (not re.match('\S{1,8}', data['password']) or len(data['password']) < 8):
                return JsonResponse({"message": 'INVALID_PASSWORD_FORMAT'}, status=400)

            if not re.match('\d{3}-\d{3,4}-\d{4}', data['phone_number']):
                return JsonResponse({"message": 'INVALID_PHONE_NUMBER_FORMAT'}, status=400)

            if User.objects.filter(email=data['email']).exists():
                return JsonResponse({"message": 'EXISTED_EMAIL'}, status=400)

            User.objects.create(
                name         = data['name'],
                email        = data['email'],
                password     = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt()).decode('utf-8'),
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

            if not User.objects.filter(email=data['email']).exists():
                return jsonresponse({"message": "INVALID_USER"}, status=401)

            if not bcrypt.checkpw(data['password'].encode('utf-8'), User.objects.get(email=data['email']).password.encode('utf-8')):
                return JsonResponse({"message": "INVALID_USER"}, status=401)
            
            token = jwt.encode({'id': User.objects.get(email=data['email']).id}, SECRET_KEY, algorithm='HS256')
            return JsonResponse({"token": token}, status=200)
        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)
