import json, re

from django.http     import JsonResponse
from django.views    import View

from users.models    import User

class SignUpView(View):
    def post(self, request):
        try:
            data                = json.loads(request.body)
            email_validation    = re.compile("^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$")
            password_validation = re.compile("^(?=.*[A-Za-z])(?=.*\d)(?=.*[$@$!%*#?&])[A-Za-z\d$@$!%*#?&]{8,}$")

            if data['email']=="" or data['password']=="":
                return JsonResponse({"Message":"NO_INPUT_DATA"}, status=400)
            
            if (email_validation.match(data['email']) is None) or (password_validation.match(data['password']) is None):
                return JsonResponse({"MESSAGE":"INVALID_FORMAT"}, status=400)

            if User.objects.filter(email = data['email']).exists():
                return JsonResponse({"MESSAGE":"DATA_ALREADY_EXIST"}, status=400)
            
            if User.objects.filter(nickname = data['nickname']).exists():
                return JsonResponse({"MESSAGE":"DATA_ALREADY_EXIST"}, status=400)

            User.objects.create(
                name            = data['name'],
                email           = data['email'],
                password        = data['password'],
                phone_number    = data['phone_number'],
                age             = data['age'],
                nickname        = data['nickname']
            )
            return JsonResponse({"MESSAGE":"SUCCESS"}, status=201)
        except KeyError:
            return JsonResponse({"MESSAGE":"KEY_ERROR"}, status=400)

class SignInView(View):
    def post(self, request):
        try:
            data                = json.loads(request.body)

            if data['email']=="" or data['password']=="":
                return JsonResponse({"MESSAGE":"NO_INPUT_DATA"}, status=400)
            
            if not User.objects.filter(email = data['email']).exists():
                return JsonResponse({"MESSAGE":"INVALID_USER"}, status=401)

            if User.objects.get(email = data['email']).password != data['password']:
                return JsonResponse({"MESSAGE":"INVALID_USER"}, status=401)

            return JsonResponse({"MESSAGE":"SUCCESS"}, status=200)
        except KeyError:
            return JsonResponse({"MESSAGE":"KEY_ERROR"}, status=400)