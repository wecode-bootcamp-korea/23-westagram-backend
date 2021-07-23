import json
import re

from django.http import JsonResponse
from django.views import View

from users.models import User

class UserView(View):
    def post(self, request):
        data = json.loads(request.body)
        email = data.get('email') # data.get('email')
        password = data.get('password')

        # email 혹은 password를 request로 전달받지 못했을 때  
        if email == None or password == None:
            return JsonResponse({'MESSAGE': 'KEY_ERROR'}, status = 400)
        
        # password에 공백을 포함하거나 8자리 이상으로 입력하지 않았을 때
        password_p = re.compile('\s')
        password_m = password_p.search(data['password'])
        if password_m != None:
            return JsonResponse({'MESSAGE' : '비밀번호는 공백을 포함할 수 없습니다.'}, status = 400)
        elif len(data['password']) < 8:
            return JsonResponse({'MESSAGE' : '비밀번호는 8자리 이상을 입력해야 합니다.'})

        # 이메일에 @ 혹은 . 이 포함되지 않을 때
        email_p = re.compile('[\w]+@[\w]+[.]+[\w]+')
        email_m = email_p.match(data['email'])
        if email_m == None:
            return JsonResponse({'MESSAGE' : '양식에 맞게 이메일을 다시 작성해주세요.'})

        # 회원가입시 db에 이미 같은 이메일이 있을 때
        if User.objects.filter(email=data['email']).exists():
            return JsonResponse({'MESSAGE' : "이미 존재하는 이메일입니다."}, status = 400)

        user = User.objects.create(
            name = data['name'],
            email = data['email'],
            password = data['password'],
            phone_number = data['phone_number'],
            age = data['age']
        )

        return JsonResponse({'MESSAGE' : "SUCCESS"}, status=201)