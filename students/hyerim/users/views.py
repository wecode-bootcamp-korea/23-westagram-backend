import json
import re

from django.http import JsonResponse
from django.views import View

from users.models import User

# Create your views here.

class SignupView(View):
  def post(self, request):
    try: 
      data = json.loads(request.body)
      
      if User.objects.filter(email=data["email"]).exists():
        return JsonResponse({"message":"EMAIL_ALREADY_EXISTS"}, status=400)  

<<<<<<< HEAD
=======
      if User.objects.filter(user_id=data["user_id"]).exists():
        return JsonResponse({"message":"ID_ALREADY_EXISTS"}, status=400)    
      
>>>>>>> da4de021c4b88acd23e8950922b4f65925d024b7
      email_type = re.compile('^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
      password_type = re.compile('^(?=.*[A-Za-z])(?=.*\d)(?=.*[$@$!%*#?&])[A-Za-z\d$@$!%*#?&]{8,}$')
      id_type = re.compile('^[a-z]{3,}[0-9]{3,}$')

      if (not email_type.match(data["email"])):
        return JsonResponse({"message":"EMAIL_FORMAT_ERROR"}, status=401)

      if (not id_type.match(data["user_id"])):
        return JsonResponse({"message":"ID_FORMAT_ERROR"}, status=401)

      if (not password_type.match(data["password"])):
        return JsonResponse({"message":"PASSWORD_FORMAT_ERROR"}, status=401)
      
      User.objects.create(
        name       = data["name"],
        email      = data["email"],
        user_id    = data["user_id"],
        password   = data["password"],
        mobile     = data["mobile"],
        address    = data["address"],
        birth_date = data["birth_date"]
        )
      return JsonResponse({"message":"SUCCESS"}, status=201)
      
    except:
      return JsonResponse({"message":"KEY_ERROR"}, status=400)

     

