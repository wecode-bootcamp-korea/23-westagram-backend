from django.http.response   import JsonResponse
from users.models           import User
from my_settings            import SECRET_KEY
from django.core.exceptions import ObjectDoesNotExist     
import jwt 



def token_reader(func):
    def wrapper(self, request, *args, **kwargs):
        try:
            token        = request.headers.get('Authorization', None)
            payload      = jwt.decode(token, SECRET_KEY, algorithms='HS256')
            user         = User.objects.get(id=payload['id'])
            request.user = user
        
        except jwt.exceptions.DecodeError:
            return JsonResponse({'message' : 'INVALID_TOKEN' }, status=400)

        except User.DoesNotExist:
            return JsonResponse({'message' : 'INVALID_USER'}, status=400)

        return func(self, request, *args, **kwargs)

    return wrapper

            

