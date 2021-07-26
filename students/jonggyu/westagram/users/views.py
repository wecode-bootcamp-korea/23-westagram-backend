import json, re, bcrypt, jwt

from django.views        import View
from django.http         import JsonResponse

from .models             import User
from westagram.settings  import SECRET_KEY

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
                password      = bcrypt.hashpw(data["password"].encode('utf-8'), bcrypt.gensalt()).decode('utf-8'),
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

            if not bcrypt.checkpw(data["password"].encode('utf-8'), User.objects.get(email = data["email"]).password.encode('utf-8')):
                return JsonResponse({"message": "INVALID_USER"}, status=401)

            return JsonResponse({"token": jwt.encode({'user_id' : User.objects.get(email = data["email"]).id}, SECRET_KEY, algorithm = 'HS256')}, status=200)

        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)