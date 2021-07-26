import json, re

from django.views   import View
from django.http    import JsonResponse

from .models        import User

class UserView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)

            if (data["password"] == "") or (data["email"] == ""):
                return JsonResponse({"message": "EMPTY_PASSWORD_OR_EMAIL"}, status=400)

            if re.match(r"^[a-zA-Z0-9+._-]+@[a-zA-Z0-9]+\.[a-zA-Z0-9-.]{2,4}$", data["email"]) is None:
                return JsonResponse({"message": "INVALID_FORMAT"}, status=400)

            if re.match(r"^(?=.*[A-Za-z])(?=.*\d)(?=.*[$@$!%*#?&])[A-Za-z\d$@$!%*#?&]{8,}$" ,data["password"]) is None:
                return JsonResponse({"message": "INVALID_FORMAT"}, status=400)

            if User.objects.filter(email = data["email"]).exists():
                return JsonResponse({"message": "RESISTERED_EMAIL"}, status=400)

            User.objects.create(
                name          = data["name"],
                email         = data["email"],
                password      = data["password"],
                phone_number  = data["phone_number"],
                age           = data["age"]
            )
            return JsonResponse({"message": "SUCCESS"}, status=201)

        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)

class UserLoginView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)

            if (data["password"] == "") or (data["email"] == ""):
                return JsonResponse({"message": "EMPTY_PASSWORD_OR_EMAIL"}, status=400)

            if not User.objects.filter(email = data["email"]).exists():
                return JsonResponse({"message": "INVALID_USER"}, status=401)

            if User.objects.get(email=data["email"]).password != data["password"]:
                return JsonResponse({"message": "INVALID_USER"}, status=401)

            return JsonResponse({"message": "SUCCESS"}, status=200)

        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)