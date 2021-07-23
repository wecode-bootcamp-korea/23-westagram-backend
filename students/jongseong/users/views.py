import json, re

from django.http     import JsonResponse
from django.views    import View

from users.models    import User

class UsersView(View):
    def post(self, request):
        try:
            data                = json.loads(request.body)
            email_validation    = re.compile("^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$")
            password_validation = re.compile("^(?=.*[A-Za-z])(?=.*\d)(?=.*[$@$!%*#?&])[A-Za-z\d$@$!%*#?&]{8,}$")

            if data['email']=="" or data['password']=="":
                return JsonResponse({"Message":"KEY_ERROR"}, status=400)
            
            if (email_validation.match(data['email']) is None) or (password_validation.match(data['password']) is None):
                return JsonResponse({"MESSAGE":"INVALID_FORMAT"}, status=400)

            if User.objects.filter(email = data['email']).exists():
                return JsonResponse({"MESSAGE":"EMAIL_ALREADY_EXIST"}, status=400)

            user = User.objects.create(
                name            = data['name'],
                email           = data['email'],
                password        = data['password'],
                phone_number    = data['phone_number'],
                age             = data['age']
            )
            return JsonResponse({"MESSAGE":"SUCCESS"}, status=201)
        except KeyError:
            return JsonResponse({"MESSAGE":"KEY_ERROR"}, status=400)

