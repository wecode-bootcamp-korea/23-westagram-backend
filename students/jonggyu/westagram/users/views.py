from django.views   import View
from django.http    import JsonResponse
from .models        import User
import json
import re

class UserView(View):
    def post(self, request):
        data = json.loads(request.body)

        if (data["email"] == "") or (data["password"] == ""):
            return JsonResponse({"message": "ERROR_EMPTY_EMAIL_PASSWORD"}, status=400)

        if re.match(r"^[a-zA-Z0-9+._-]+@[a-zA-Z0-9]+\.[a-zA-Z0-9-.]{2,4}$", data["email"]) == None:
            return JsonResponse({"message": "ERROR_EMAIL_NEED_@AND."}, status=400)

        if re.match(r"^(?=.*[A-Za-z])(?=.*\d)(?=.*[$@$!%*#?&])[A-Za-z\d$@$!%*#?&]{8,}$" ,data["password"]) == None:
            return JsonResponse({"message": "ERROR_PASSWORD(NEED_OVER8_AND_ALPHABET,NUMBER,SPECIAL_SYMBOLS)"}, status=400)

        if User.objects.filter(email = data["email"]).count() == 1:
            return JsonResponse({"message": "ERROR_RESISTERED_EMAIL"}, status=400)

        User.objects.create(
            name          = data["name"],
            email         = data["email"],
            password      = data["password"],
            phone_number  = data["phone_number"],
            age           = data["age"]
        )
        return JsonResponse({"message" : "SUCCESS"}, status=201)