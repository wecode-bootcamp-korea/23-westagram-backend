import json
import re

from django.http import JsonResponse
from django.views import View

from users.models import User


class UserView(View):
    def post(self, request):
        data = json.loads(request.body)

        if ((data["email"] or data["password"]) not in data.values()):
            return JsonResponse({"message":"KEY_ERROR"}, status = 400)

        if (re.match("\w*@\w*.\w*", data["email"]) == None):
            return JsonResponse({"message":"INVALID__EMAIL"}, status = 400)

        if (re.match("[\w\W{8,20}]", data["password"]) == None):
            return JsonResponse({"message":"INVALID_PASSWORD"}, status = 400)  
        
        if User.objects.filter(email = data["email"]).exists():
            return JsonResponse({"message":"EXIST_EMAIL"}, status = 400)

        User.objects.create(
            name         = data["name"],
            email        = data["email"],
            password     = data["password"],
            phone_number = data["phone_number"],
            birth_date   = data["birth_date"]        
        )

        return JsonResponse({"message":"SUCCESS"}, status = 201)