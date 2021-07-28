import json, re, bcrypt, jwt

from django.views        import View
from django.http         import JsonResponse

from .models             import User
from westagram.settings  import SECRET_KEY

class SignUp(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            hashed_password = bcrypt.hashpw(data['password'].encode('UTF-8'), bcrypt.gensalt())

            if User.objects.filter(email=data['email']).exists():
                return JsonResponse({"message": "EMAIL_ALREADY_EXIST"}, status=400)

            if (data['email'] == '') or (data['password'] == ''):
                return JsonResponse({"message": "NO_INPUT"}, status=400)

            if re.match(r"^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", data['email']) is None:
                return JsonResponse({"message": "INVALID_FORMAT"}, status=400)

            if re.match(r"^(?=.*[A-Za-z])(?=.*\d)(?=.*[$@$!%*#?&])[A-Za-z\d$@$!%*#?&]{8,}$", data['password']) is None:
                return JsonResponse({"message": "INVALID_FORMAT"}, status=400)

            User.objects.create(
                # name         =   data['name'],
                email        =   data['email'],
                password     =   hashed_password.decode('UTF-8'),
                # phone_number =   data['phone'],
                # age          =   data['age']
            )

            return JsonResponse({"Message": "SUCCESS"}, status=201)
        
        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)

class SignIn(View):
    def post(self, request):
        try:
            data = json.loads(request.body)

            if (data['email'] == '') or (data['password'] == ''):
                return JsonResponse({"message": "KEY_ERROR"}, status=400)

            if not User.objects.filter(email=data['email']).exists():
                return JsonResponse({"message": "INVALID_USER"}, status=401)
            
            user = User.objects.get(email=data['email'])

            if not bcrypt.checkpw(data['password'].encode('UTF-8'), user.password.encode('UTF-8')):
                return JsonResponse({"massage": "INVALID_USER"}, status=401)

            token = jwt.encode({'user_id': user.id}, SECRET_KEY, algorithm='HS256')
            
            return JsonResponse({'token': token}, status = 200)

        except KeyError:
            return JsonResponse({"massage": "KEY_ERROR"}, status=400)