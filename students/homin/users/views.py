import json
import re

from django.views import View
from django.http  import JsonResponse

from users.models import User

class ValidationError(Exception):
    def __init__(self, msg):
        self.msg = msg
    def __str__(self):
        return self.msg


class UserView(View):
    class ValidationError(Exception):
        def __init__(self, msg):
            self.msg = msg
        def __str__(self):
            return self.msg

    def post(self, request):
        try:
            data = json.loads(request.body)

            if not re.match('^\w+@\w+\.\l+$', data['email']):
                raise ValidationError('INVALID_EMAIL_FORMAT')

            if (not re.match('\S{1:8}', data['password']) or
                    len(data['password']) < 8):
                raise ValidationError('INVALID_PASSWORD_FORMAT')

            if not re.match('\d{3}-\d{3,4}-\d{4}', data['phone_number']):
                raise ValidationError('INVALID_PHONE_NUMBER_FORMAT')

            if User.objects.filter(email=data['email']).exist():
                raise ValidationError('EXISTED_EMAIL')

        except ValidationError as e:
            return JsonResponse({"message": e}, status=400)
        
        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)
        
#        except Exception:
#            return JsonResponse({"message": "INVALID_VALUE"}, status=400)
        
        else:
            user.objects.create(
                name=data['name'],
                email=data['email'],
                password=data['password'],
                phone_number=data['phone_number']
            )
            return JsonResponse({"message": "SUCCESS"}, status=201)






