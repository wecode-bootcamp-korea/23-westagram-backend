import json
import re
import bcrypt

from django.http import JsonResponse
from django.views import View

from users.models import User


class UserView(View):
    def post(self, request):
        data = json.loads(request.body)

        try:
            if (re.match("\w*@\w*.\w*", data["email"]) is None):
                return JsonResponse({"message":"INVALID__EMAIL"}, status = 400)

            if (re.match("[\w\W{8,20}]", data["password"]) is None):
                return JsonResponse({"message":"INVALID_PASSWORD"}, status = 400)  
            
            if User.objects.filter(email = data["email"]).exists():
                return JsonResponse({"message":"EXIST_EMAIL"}, status = 400)

            hashed_password = bcrypt.hashpw(data["password"].encode("utf-8"), bcrypt.gensalt())

            User.objects.create(
                name         = data["name"],
                email        = data["email"],
                password     = hashed_password.decode("utf-8"),
                phone_number = data["phone_number"],
                birth_date   = data["birth_date"]        
            )

            return JsonResponse({"message":"SUCCESS"}, status = 201)

        except KeyError:
            return JsonResponse({"message":"KEY_ERROR"}, status = 400)

class LoginView(View):
    def post(sef, request):
        data = json.loads(request.body)

        try:
            if data["email"] == "" or data["password"] == "":
                return JsonResponse ({"message":"INVALID_USER"}, status = 401)

            if not User.objects.filter(email = data["email"]).exists():
                return JsonResponse({"message":"INVALID_USER"}, status = 401)

            user = User.objects.get(email = data["email"])
            
            if not bcrypt.checkpw(data["password"].encode("utf-8"), user.password.encode("utf-8")):
                return JsonResponse({"message":"INVALID_USER"}, status = 401)

            return JsonResponse({"message":"SUCCESS"}, status = 200)

        except KeyError:
            return JsonResponse({"message":"KEY_ERROR"}, status = 400)            

