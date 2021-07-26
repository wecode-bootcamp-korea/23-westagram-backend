import jwt, json

from django.http import JsonResponse

from users.models import User
from westagram.settings import SECRET_KEY

def Keep_signup(func):
    def wrap(self,request):
        receive_token = request.header.get('Authorization')
        receive_id = jwt.decode(receive_id, SECRET_KEY, algorithms='HS256')
        if receive_id == User.objects.get(id):
            return JsonResponse({'MESSAGE':'VALID_TOKEN'}, status=200)
        return JsonResponse({'MESSAGE':'INVALID_TOKEN'}, status=400)
    return wrap