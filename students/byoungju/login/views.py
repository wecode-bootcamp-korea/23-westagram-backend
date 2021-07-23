import json
import re

from django.http import JsonResponse
from django.views import View

from users.models import User

class LoginView(View):
    def post(sef, request):
        data = json.loads(request.body)

        try:
            if (User.objects.filter(email = data["email"]).exists() and \
                User.objects.filter(password = data["password"]).exists()):
                return JsonResponse({"message":"SUCCESS"}, status = 200)
            else:
                return JsonResponse({"message":"INVALID_USER"}, status = 401)
            
        except KeyError:
            return JsonResponse({"message":"KEY_ERROR"}, status = 400)
