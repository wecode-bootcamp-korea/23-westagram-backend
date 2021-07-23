from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from users.models import User
import json
import re

class User_CreateView(View):
    def post(self, request):
        data = json.loads(request.body)

        try:
            data['email'] == "" or data['password'] == ""
        except KeyError:
            return JsonResponse({'MESSAGE':'KEY_ERROR'}, status = 400)

        '''if data['email'] == None or data['password'] == None:
            return JsonResponse({'MESSAGE':'KEY_ERROR'}, status = 400)'''

        if User.objects.filter(email = data['email']).exists():
            return JsonResponse({'MESSAGE':'USE_OTHER_EMAIL'}, status = 400)
        
        email_check = re.compile('^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
        emails = data['email']
        if email_check.match(emails) == None:
            return JsonResponse({'MESSAGE':'CHECK_EMAIL_FOAM'}, status = 400)
        
        password_check = re.compile("^(?=.*[A-Za-z])(?=.*\d)(?=.*[$@$!%*#?&])[A-Za-z\d$@$!%*#?&]{8,}$")
        passwords = data['password']
        if password_check.match(passwords) == None:
            return JsonResponse({'MESSAGE':'CHECK_PASSWORD_FOAM'}, status = 400)            

        user = User.objects.create(
            name         = data['name'],
            email        = emails,
            password     = passwords,
            phone_number = data['phone_number'],
            address      = data.get('address'),
            birth_date   = data.get('birth_date'),
            nickname     = data.get('nickname')
            )
        return JsonResponse({'MESSAGE':'SUCCESS'}, status = 201)

