import json
import re

from django.http import JsonResponse
from django.views import View
from users.models import User

# Create your views here.

class UserView(View):
  def post(self, request):
    data = json.loads(request.body)
    
    email_type = re.compile('^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
    password_type = re.compile('^(?=.*[A-Za-z])(?=.*\d)(?=.*[$@$!%*#?&])[A-Za-z\d$@$!%*#?&]{8,}$')
    
    if User.objects.filter(data["email"]).exists:
      return JsonResponse({"message":"EMAIL_ALREADY_EXISTS"}, status=400)  

    if (not email_type.match(data["email"])) or (not password_type.match(data["password"])):
      return JsonResponse({"message":"INPUT_FORMAT_ERROR"}, status=401)
    
    else:
      try: 
        User.objects.create(
          name       = data["name"],
          email      = data["email"],
          password   = data["password"],
          mobile     = data["mobile"],
          address    = data["address"],
          birth_date = data["birth_date"]
        )
        return JsonResponse({"message":"SUCCESS"}, status=201)
      except:
        return JsonResponse({"message":"KEY_ERROR"}, status=400)

