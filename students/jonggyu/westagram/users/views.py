import json, re

from django.views   import View
from django.http    import JsonResponse

from .models        import User

class UserView(View):
    def post(self, request):
        data = json.loads(request.body)

        if (data["password"] == "") or (data["email"] == ""):
            return JsonResponse({"message": "KEY_ERROR"}, status=400)

        if re.match(r"^[a-zA-Z0-9+._-]+@[a-zA-Z0-9]+\.[a-zA-Z0-9-.]{2,4}$", data["email"]) == None:
            return JsonResponse({"message": "INVALID_FORMAT"}, status=400)

        if re.match(r"^(?=.*[A-Za-z])(?=.*\d)(?=.*[$@$!%*#?&])[A-Za-z\d$@$!%*#?&]{8,}$" ,data["password"]) == None:
            return JsonResponse({"message": "INVALID_FORMAT"}, status=400)

        if User.objects.filter(email = data["email"]).exists():
            return JsonResponse({"message": "RESISTERED_EMAIL"}, status=400)

        try:
            User.objects.create(
                name          = data["name"],
                email         = data["email"],
                password      = data["password"],
                phone_number  = data["phone_number"],
                age           = data["age"]
            )

        except:
            return JsonResponse({"message": "EMPTY_INFORMATION"}, status=400)

        else:
            return JsonResponse({"message": "SUCCESS"}, status=201)