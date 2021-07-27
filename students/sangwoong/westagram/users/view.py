import json
import bcrypt
import jwt

from django.http  import JsonResponse 
from django.views import View

from .models	        import User
from westagram.settings import SECRET_KEY




class UserView(View):
    def post(self,request):
        try:
            data = json.loads(request.body)
            
            MINIMUM_PASSWORD_LENGTH = 8
            if '@' not in data['email'] or '.' not in data['email']:
                return JsonResponse({'MESSAGE' : 'INVALID EMAIL'}, status=400)

            if len(data['password']) < MINIMUM_PASSWORD_LENGTH:
                return JsonResponse({'MESSAGE' : 'INVALID PASSWORD'}, status=400)

            if User.objects.filter(email=data['email']).exists():
                return JsonResponse({'MESSAGE' : 'DUPLICATED EMAIL'}, status=400)

            if User.objects.filter(phone_number=data['phone_number']).exists():
                return JsonResponse({'MESSAGE' : 'DUPLICATED PHONE_NUM'}, status=400)

            if User.objects.filter(name=data['name']).exists():
                return JsonResponse({'MESSAGE' : 'DUPLICATED NAME'}, status=400)

            hashed_password = bcrypt.hashpw (data['password'].encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

              
            User.objects.create(
                name          = data['name'],
                phone_number  = data['phone_number'],
                password      = hashed_password,
                email         = data['email']
            )
            return JsonResponse({'MESSAGE' : 'SUCCESS'}, status=201) 
        except KeyError:
            return JsonResponse({'MESSAGE' : 'KEY ERROR'}, status=400)

class SigninView(View):
    def post(self, request):
        try:
            data     = json.loads(request.body)
            user     = User.objects.get(email=data['email'])
            password = data['password']

            if data['email']=="" or data['password']=="":
                return JsonResponse({"MESSAGE":"NOT_FOUND"},status=404)
            
            if not User.objects.filter(email=data['email']).exists():
                return JsonResponse({"MESSAGE" : "INVALID_USER"}, status=401)
            
            if not bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
                return JsonResponse({'MESSAGE':'INVALID_USER'}, status=401)

            access_token = jwt.encode({'id' : user.id}, SECRET_KEY, algorithm = 'HS256').decode()
            return JsonResponse({'MESSAGE':'SUCCESS', 'TOKEN': access_token },status=200)
        except KeyError:
            return JsonResponse({"MESSAGE" : "KEY_ERROR"}, status=400)
