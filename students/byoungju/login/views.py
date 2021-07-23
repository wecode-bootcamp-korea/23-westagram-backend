import json
import re

from django.http import JsonResponse
from django.views import View

from users.models import User

class LoginView(View):
    def post(sef, request):
        data     = json.loads(request.body)
 
        try:
            if (data["email"] or data["password"] == ""):
                return JsonResponse ({"message":"INVALID_USER"}, status = 401)

            if not (User.objects.filter(email = data["email"]).exists()):
                return JsonResponse({"message":"INVALID_USER"}, status = 401)

            user = User.objects.get(email = data["password"])

            if (user.password != data["password"]):
                return JsonResponse({"message":"INVALID_USER"}, status = 401)

            return JsonResponse({"message":"SUCCESS"}, status = 200)

        except KeyError:
            return JsonResponse({"message":"KEY_ERROR"}, status = 400)
        