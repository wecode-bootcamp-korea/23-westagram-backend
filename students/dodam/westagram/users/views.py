import re
import json

from django.http import JsonResponse
from django.views import View
from users.models import User
from django.db import IntegrityError

password_regular = re.compile("^(?=.*[A-Za-z])(?=.*\d)(?=.*[$@$!%*#?&])[A-Za-z\d$@$!%*#?&]{8,}$")

class UserView(View):
	def post(self,request):
		try:	
			data = json.loads (request.body) # 프론트가 requset한 정보를 바디에 담아 json 을 활용해 읽어내겠다는 의미 
			# 중복에러 설정하기
			if User.objects.filter(name=data['name']).exists():
				return JsonResponse({'MESSAGE': 'INVALID_FORMAT'}, status = 400)

			if User.objects.filter(email=data['email']).exists():
				return JsonResponse({'MESSAGE': 'INVALID_FORMAT'}, status = 400)		

			# 이메일 필수조건 설정해주기
			if ('@' not in data['email']) or ('.'not in data['email']):
				return JsonResponse({'MESSAGE': 'INVALID_FORMAT'}, status = 400)				

			# 패스워드 설정 관련 정규식 : 8자이상, 문자, 숫자, 특수문자 조건 충족
			if not password_regular.match(data['password']):
				return JsonResponse ({'MESSAGE': 'INVALID_FORMAT'}, status = 400)


			User.objects.create(
			name 		 = data['name'],
			email	 	 = data['email'],
			password	 = data['password'],
			phone_number = data['phone_number'], 
			birthday 	 = data['birthday'],
			)
			return JsonResponse ({'MESSAGE' : 'SUCCESS'}, status = 201)

		except KeyError: # 키 값이 빠진다면 나오는 오류
			return JsonResponse ({'MESSAGE': 'KEY_ERROR'}, status = 400)

		except IntegrityError: # email = unique=ture 설정을 사용하여 지정해준 에러값
			return JsonResponse ({'MESSAGE': 'INTERGRITY_ERROR'}, status = 400)




			# 이메일 글자 수 8자 미만 오류 발생_  글자수로만 지정하면 특수문자 반영을 할 수 없다
			# if len(data['password']) < 8: 
			#	return JsonResponse({'MESSAGE' : '비밀번호는 8자 이상으로 설정해주세요.'},status = 400)