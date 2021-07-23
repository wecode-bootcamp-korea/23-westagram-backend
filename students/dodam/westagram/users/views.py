import json, re

from django.views import View
from django.http import JsonResponse

from users.models import User

password_regular = re.compile("^(?=.*[A-Za-z])(?=.*\d)(?=.*[$@$!%*#?&])[A-Za-z\d$@$!%*#?&]{8,}$")

class UserView(View):
	def post(self,request):
		try:	
			data = json.loads (request.body) # 프론트가 requset한 정보를 바디에 담아 json 을 활용해 읽어내겠다는 의미 
			# 중복에러 설정하기
			if User.objects.filter(name=data['name']).exists(): 
				if User.objects.filter(email=data['email']).exists(): 			
					return JsonResponse({'MESSAGE': 'DATA_OVERLAP'}, status = 400)		

			# 이메일 필수조건 설정 및 패스워드 설정 관련 정규식 : 8자이상, 문자, 숫자, 특수문자 조건 충족
			if ('@' not in data['email']) or ('.'not in data['email']):		
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