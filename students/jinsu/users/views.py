import json
import re

from django.http  import JsonResponse
from django.views import View
from users.models import User

class UserView(View):
    def post(self,request):
        data = json.loads(request.body)

        # 필수 기입 정보(이메일, 비밀번호) 포함 여부 확인
        try:
            data['email']
        except KeyError:
            return JsonResponse({"message":"KEY_ERROR"}, status=400)
        
        try:
            data['password']
        except KeyError:
            return JsonResponse({"message":"KEY_ERROR"}, status=400)

        # 이메일 형식 확인(@, . 필수 포함!  e.g. 'bbb@ccc.com')
        email_validation = re.compile('\w+[@]\w+[.]\w+')

        if not email_validation.match(data['email']):
            return JsonResponse({"message":"INVALID_EMAIL_FORMAT"}, status=400)

        # 비밀번호 형식 확인(8자리 이상, 문자/숫자/특수문자 복합)
        password_validation = re.compile('\S{8,}')

        if not password_validation.match(data['password']):
            return JsonResponse({"message":"PASSWORD_TOO_SHORT"}, status=400)

        # 이메일 중복 여부 확인
        if User.objects.filter(email=data['email']).exists():
            return JsonResponse({"message":'EMAIL_ALREADY_EXISTS'}, status=400)

        # 모든 조건 만족시 가입 정보를 DB에 생성
        user = User.objects.create(
            name         = data['name'],
            email        = data['email'],
            password     = data['password'],
            phone_number = data['phone_number'],
            age          = data['age'],
        )

        return JsonResponse({"message":"SUCCESS"}, status=201)
        
            
