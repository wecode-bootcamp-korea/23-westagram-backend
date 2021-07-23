from django.http.response import JsonResponse
from django.views import View
import json
from users.models import User
import re

class UserView(View):
    def post(self, request):
        data=json.loads(request.body)
        Email = re.compile("^[a-zA-Z0-9+-_.]+@[a-zA-z0-9-]+\.[a-zA-z0-9-]+$")
        PW    = re.compile("^(?=.*[A-Za-z])(?=.*\d)(?=.*[$@$!%*#?&])[A-Za-z\d$@$!%*#?&]{8,}$")
        
        if  PW.match(data['password'])  == None and Email.match(data['email']) == None:
            return JsonResponse({'message':'Please check your password and email address!'}, status=400)         
        
        elif Email.match(data['email']) == None :
            return JsonResponse({'message':'Please check your email address!'}, status=400)   
        
        elif PW.match(data['password']) == None :
            return JsonResponse({'message':'Please check your password!'}, status=400)  
        else:
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

