import json, re

from django.views import View
from django.http import JsonResponse

from users.models import User

class User_View(View):
    def post(self, request):
        try:
            data = json.loads(request.body)               
            if data['email'] == "" or data['password'] == "":
                return JsonResponse({'MESSAGE':'INVALID_VALUE'}, status = 401)
        
            if User.objects.filter(email = data['email']).exists():
                return JsonResponse({'MESSAGE':'USE_OTHER_EMAIL'}, status = 400)
            
            email_check = re.compile('^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
            emails = data['email']
            if email_check.match(emails) is None:
                return JsonResponse({'MESSAGE':'CHECK_EMAIL_FOAM'}, status = 400)
            
            password_check = re.compile("^(?=.*[A-Za-z])(?=.*\d)(?=.*[$@$!%*#?&])[A-Za-z\d$@$!%*#?&]{8,}$")
            password = data['password']
            if password_check.match(password) is None:
                return JsonResponse({'MESSAGE':'CHECK_PASSWORD_FOAM'}, status = 400)            

            User.objects.create(
                name         = data['name'],
                email        = emails,
                password     = password,
                phone_number = data['phone_number'],
                address      = data.get('address'),
                birth_date   = data.get('birth_date'),
                nickname     = data.get('nickname')
                )
            return JsonResponse({'MESSAGE':'SUCCESS'}, status = 201)

        except KeyError:
            return JsonResponse({'MESSAGE':'KEY_ERROR'}, status = 400)
