import json
import re

from django.http import JsonResponse
from django.views import View
from django.core.exceptions import ObjectDoesNotExist

from users.models import User

class LoginView(View):
    def post(sef, request):
        data     = json.loads(request.body)
        email    = data["email"]
        password = data["password"]

        try:

            if (User.objects.get(email = email) and \
                User.objects.filter(password = password).exists()):
                return JsonResponse({"message":"SUCCESS"}, status = 200)
            else:
                return JsonResponse({"message":"INVALID_USER"}, status = 401)
            
        except KeyError:
            return JsonResponse({"message":"KEY_ERROR"}, status = 400)

        except ObjectDoesNotExist:
            return JsonResponse({"message":"INVALID_USER"}, status = 401)

