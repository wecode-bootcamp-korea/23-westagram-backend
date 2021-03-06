import json, re, bcrypt, jwt

from django.http  import JsonResponse
from django.views import View

from users.models import User
from my_settings  import SECRET_KEY

def email_validation(email):
    p = re.compile('^[a-zA-Z0-9-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-_]+\.*[a-zA-Z0-9-_]+$')
    return not p.match(email)

def password_validation(password):
    p = re.compile('^[A-Za-z\d$@$()^!%*#?&].{7,}$')
    return not p.match(password)

class SignUpView(View):
    def post(self, request):
        data = json.loads(request.body)
        
        try:
            email        = data['email']
            password     = data['password']
            phone_number = data['phone_number']
            if email_validation(email): 
                return JsonResponse({"MESSAGE":"INVALID_EMAIL"}, status=400)
            
            if password_validation(password): 
                return JsonResponse({"MESSAGE":"INVALID_PASSWORD"}, status=400)
            
            if User.objects.filter(email=email).exists(): 
                return JsonResponse({"MESSAGE":"ALREADY_EMAIL_EXSISTS"}, status=400)

            if User.objects.filter(phone_number=phone_number).exists(): 
                return JsonResponse({"MESSAGE":"ALREADY_PHONE_NUMBER_EXSISTS"}, status=400)

            hashed_password = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

            User.objects.create(
                name         = data['name'],
                email        = data['email'],
                password     = hashed_password,
                phone_number = data['phone_number'],
                age          = data['age'],
                gender       = data['gender'],
                birth_date   = data['birth_date']
            )
            return JsonResponse({"MESSAGE": "SUCCESS"}, status=201)
        except KeyError:
            return JsonResponse({"MESSAGE":"KEY_ERROR"},status=400)

class LoginView(View):
    def post(self, request):
        data = json.loads(request.body)

        try:
            if not User.objects.filter(email=data['email']).exists():
                return JsonResponse({"MESSAGE":"INVALID_USER"}, status=401)
            
            user = User.objects.get(email=data['email'])

            check_password = bcrypt.checkpw(data['password'].encode('utf-8'), user.password.encode('utf-8'))
            
            if not check_password:
                return JsonResponse({"MESSAGE":"INVALID_USER"}, status=401)

            access_token = jwt.encode({'id':user.id}, SECRET_KEY, algorithm='HS256')
            
            return JsonResponse({"token":access_token}, status=200) 
        except KeyError:
            return JsonResponse({"MESSAGE":"KEY_ERROR"},status=400)

        