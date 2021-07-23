from django.http.response import JsonResponse
from django.views import View
import json
from users.models import User
import re

class UserView(View):
    def post(self, request):
        data=json.loads(request.body)
        p = re.compile("^[a-zA-Z0-9+-_.]+@[a-zA-z0-9-]+\.[a-zA-z0-9-]+$")
        # q = re.compile("^(?=.*[A-Za-z])(?=.*\d)(?=.*[$@$!%*#?&])[A-Za-z\d$@$!%*#?&]{8,}$")
        if p.match(data['email']) == None :
            return JsonResponse({'message':'check your email address'}, status=404)   
        else:
            User.objects.create(
                name          = data['name'],
                email         = data['email'],
                password      = data['password'],
                phone_numbers = data['phone_numbers'],
                web_site      = data['website'],
                nick_name     = data['nick_name'],
                address       = data['address'],
                introduce     = data['introduce']
            )
            return JsonResponse({'message': 'created'}, status=201)




                    # elif data['email'] =='' or data['password']=='' or  data['address']=='' or  data['name']=='':
        #     return JsonResponse({'message':'check your profile'}, status=404)