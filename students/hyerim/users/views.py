import json
import re
import bcrypt
import jwt

from django.http import JsonResponse
from django.views import View

from users.models import User

# Create your views here.

class SignupView(View):
  def post(self, request):
    try: 
      data = json.loads(request.body)
      
      if User.objects.filter(email=data['email']).exists():
        return JsonResponse({'message':'EMAIL_ALREADY_EXISTS'}, status=400)  

      email_type = re.compile('^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
      password_type = re.compile('^(?=.*[A-Za-z])(?=.*\d)(?=.*[$@$!%*#?&])[A-Za-z\d$@$!%*#?&]{8,}$')

      if not email_type.match(data['email']):
        return JsonResponse({'message':'EMAIL_FORMAT_ERROR'}, status=401)

      if not password_type.match(data['password']):
        return JsonResponse({'message':'PASSWORD_FORMAT_ERROR'}, status=401)

      hashed_password = bcrypt.hashpw(
        data['password'].encode('utf-8'),bcrypt.gensalt()
        ).decode()
      
      User.objects.create(
        name       = data['name'],
        email      = data['email'],
        password   = hashed_password,
        mobile     = data['mobile'],
        address    = data['address'],
        birth_date = data['birth_date']
        )
      return JsonResponse({'message':'SUCCESS'}, status=201)
      
    except:
      return JsonResponse({'message':'KEY_ERROR'}, status=400)

class SigninView(View):
    def post(self, request):
      try:  
        data = json.loads(request.body)

        if not User.objects.filter(email=data['email']).exists():
          return JsonResponse({'message':'INVALID_USER'}, status=401)

        user_info = User.objects.get(email=data['email'])

        input_pw = data['password']

        user_pw = user_info.password

        if not bcrypt.checkpw(input_pw.encode('utf-8'), user_pw.encode('utf-8')):
          return JsonResponse({'message':'INVALID_USER'}, status=401) 

        return JsonResponse({'message':'SUCCESS'}, status=200)
      
      except:
        return JsonResponse({"message":"KEY_ERROR"}, status=400)

