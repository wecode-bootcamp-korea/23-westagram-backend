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
            PW    = re.compile("^(?=.*[A-Za-z])(?=.*\d)(?=.*[$@$!%*#?&])[A-Za-z\d$@$!%*#?&]{8,}$")
       
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

            if User.objects.filter(email = data["email"]).exists():
                return JsonResponse({"message": "ALREADY_EXISTS"}, status=400)

        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)







# class LoginView(View):
#     def post(self, request):

#         data      = json.loads(request.body)
#         users     = User.objects.all()
#         emails    = [i.email for i in users]
#         passwords = [j.password for j in users]

#         if data['email'] not in emails:
#             return JsonResponse({"message": "INVALID_USER"}, status=401)
        
#         elif data['password'] not in passwords:
#             return JsonResponse({"message": "INVALID_USER"}, status=401)
        
#         else:
#             return JsonResponse({'message': "SUCCESS"}, status=201)
