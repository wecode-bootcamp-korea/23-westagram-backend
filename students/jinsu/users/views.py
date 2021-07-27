import json, re, bcrypt, jwt

from django.http  import JsonResponse
from django.views import View

from users.models import User
from my_settings import SECRET_KEY

class UserView(View):
    def post(self,request):
        try:
            data = json.loads(request.body)

            email_validation    = re.compile('\w+[@]\w+[.]\w+')
            password_validation = re.compile('\S{8,}')

            if not email_validation.match(data['email']):
                return JsonResponse({"message":"INVALID_EMAIL_FORMAT"}, status=400)

            if User.objects.filter(email=data['email']).exists():
                return JsonResponse({"message":'EMAIL_ALREADY_EXISTS'}, status=400)

            if not password_validation.match(data['password']):
                return JsonResponse({"message":"PASSWORD_TOO_SHORT"}, status=400)

            hashed_password = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt())

            User.objects.create(
                name         = data['name'],
                email        = data['email'],
                password     = hashed_password.decode('utf-8'),
                phone_number = data['phone_number'],
                age          = data['age'],
            )

            return JsonResponse({"message":"SUCCESS"}, status=201)

        except KeyError:
            return JsonResponse({"message":"KEY_ERROR"}, status=400)

class LoginView(View):
    def post(self,request):
        try:
            data = json.loads(request.body)
            
            if not User.objects.filter(email=data['email']).exists():
                return JsonResponse({"message":"INVALID_USER"}, status=401)
        
            hashed_password = User.objects.get(email=data['email']).password.encode('utf-8')

            if not bcrypt.checkpw(data['password'].encode('utf-8'), hashed_password):
                return JsonResponse({"message":"INVALID_USER"}, status=401)
            
            user_id = User.objects.get(email=data['email']).id
            access_token = jwt.encode({'user_id':user_id}, SECRET_KEY, algorithm='HS256')

            return JsonResponse({"access_token":access_token}, status=200)

        except KeyError:
            return JsonResponse({"message":"KEY_ERROR"}, status=400) 
