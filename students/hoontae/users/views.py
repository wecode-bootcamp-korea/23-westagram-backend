import json
import re

from django.http       import JsonResponse
from django.views      import View

from users.models      import User
from users.validations import email_validation, password_validation

class UsersView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)

            if not email_validation(data['email']):
                return JsonResponse({'message':'INVALID_EMAIL_FORMAT'}, status=400)
            
            if not password_validation(data['password']):
                return JsonResponse({'message':'CHARACTER_SHORT'}, status=400)

            if User.objects.filter(email=data['email']).exists():
                return JsonResponse({'massage':'INVALID_EMAIL'}, status=400)

            user = User.objects.create(
                name         = data['name'],
                email        = data['email'],
                password     = data['password'],
                phone_number = data['phone_number'],
                birthday     = data['birthday'],
            )
            return JsonResponse({'message':'SUCCESS'}, status=201)
        except KeyError:
            return JsonResponse({'message':'KEY_ERROR'}, status=400)