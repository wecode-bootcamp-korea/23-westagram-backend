from django.http.response import JsonResponse
from django.views import View
from users.models import User
import re, bcrypt, jwt, json
from my_settings import SECRET_KEY

class UserView(View):
    def post(self, request):
        try:
            data       = json.loads(request.body)
            print(data)
            Email      = re.compile("^[a-zA-Z0-9+-_.]+@[a-zA-z0-9-]+\.[a-zA-z0-9-]+$")
            PW         = re.compile("^(?=.*[A-Za-z])(?=.*\d)(?=.*[~!@#$%^&*()+|=])[A-Za-z\d~!@#$%^&*()+|=]{8,16}$")
            encoded_pw = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt())
            
            if  PW.match(data['password'])  is None or Email.match(data['email']) is None:
                return JsonResponse({'message':' INVALID_FORMAT'}, status=400)         
            
            if User.objects.filter(email = data["email"]).exists():
                return JsonResponse({"message": "OVERLAP"}, status=400)

            User.objects.create(
                name          = data['name'],
                email         = data['email'],
                password      = encoded_pw.decode('utf-8'),
                phone_number  = data.get('phone_number'),
                web_site      = data.get('website'),
                nick_name     = data.get('nick_name'),
                address       = data.get('address'),
                introduce     = data.get('introduce')
            )           
            return JsonResponse({'message': "SUCCESS"}, status=201)

        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)

class LoginView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            
            if not User.objects.filter(email=data['email']).exists():
                return JsonResponse({"message": "INVALID_USER"}, status=401)
            
            user = User.objects.get(email=data['email'])
            
            if bcrypt.checkpw(data['password'].encode('utf-8'), user.password.encode('utf-8')):
                token = jwt.encode({'id': user.id}, SECRET_KEY, algorithm='HS256')
                return JsonResponse({"message": token}, status=200)              
                
            
  
        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)


