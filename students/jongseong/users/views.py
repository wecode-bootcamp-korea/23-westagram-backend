import json, re, bcrypt, jwt

from django.http        import JsonResponse
from django.views       import View

from users.models       import User
from westagram.settings import SECRET_KEY

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
            
            hashed_password = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

            User.objects.create(
                name         = data['name'],
                email        = data['email'],
                password     = hashed_password,
                phone_number = data['phone_number'],
                age          = data['age'],
                nickname     = data['nickname']
            )
            return JsonResponse({"MESSAGE":"SUCCESS"}, status=201)
        except KeyError:
            return JsonResponse({"MESSAGE":"KEY_ERROR"}, status=400)

class SignInView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            user = User.objects.get(email = data['email'])

            if data['email']=="" or data['password']=="":
                return JsonResponse({"MESSAGE":"NO_INPUT_DATA"}, status=400)
            
            if not User.objects.filter(email = data['email']).exists():
                return JsonResponse({"MESSAGE":"INVALID_USER"}, status=401)

            if not bcrypt.checkpw(data['password'].encode('utf-8'), user.password.encode('utf-8')):
                return JsonResponse({"MESSAGE":"INVALID_USER"}, status=401)

            access_token = jwt.encode({'id' : user.id}, SECRET_KEY, algorithm = 'HS256')

            return JsonResponse({"MESSAGE":"SUCCESS", "TOKEN":access_token}, status=200)
        except KeyError:
            return JsonResponse({"MESSAGE":"KEY_ERROR"}, status=400)
