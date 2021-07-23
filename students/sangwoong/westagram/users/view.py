from django.shortcuts import render

# Create your views here.
import json   # 프론트로부터 javascript 데이터 파일을 받기 위해

from django.http  import JsonResponse 
from django.views import View

from .models	  import User


class UserView(View):
    def post(self,request):
        try:
            data = json.loads(request.body)
            
            MINIMUM_PASSWORD_LENGTH = 8
            if '@' not in data['email'] or '.' not in data['email']:
                return JsonResponse({'MESSAGE' : 'INVALID EMAIL'}, status=400)
			#먄약 @나 .이 없으면 오류메세지 날림.
            if len(data['password']) < MINIMUM_PASSWORD_LENGTH:
                return JsonResponse({'MESSAGE' : 'INVALID PASSWORD'}, status=400)
            #만약 8자리이상 문자 숫자 특수문자 조합이어야함 충족되지 않으면 오류 메세지를 날림.
            if User.objects.filter(email=data['email']).exists():
                return JsonResponse({'MESSAGE' : 'DUPLICATED EMAIL'}, status=400)
            #만약 이메일 중복된다면 오류 메세지 날림.
            if User.objects.filter(phone_number=data['phone_number']).exists():
                return JsonResponse({'MESSAGE' : 'DUPLICATED PHONE_NUM'}, status=400)
            #만약 이름 중복된다면 오류 메세지 날림.
            if User.objects.filter(name=data['name']).exists():
                return JsonResponse({'MESSAGE' : 'DUPLICATED NAME'}, status=400)
			#만약 폰번호 중복된다면 오류 메세지 날림.	
              
            User.objects.create(
                name      = data['name'],
                phone_num = data['phone_num'],
                password  = data['password'],
                mail      = data['email']
            )
            return JsonResponse({'MESSAGE' : 'SUCCESS'}, status=201)  #성공하면 석세스 메세지 날림.
        except KeyError:
            return JsonResponse({'MESSAGE' : 'KEY ERROR'}, status=400)
