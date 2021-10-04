from django.http.response import JsonResponse
from django.views         import View
from users.models         import User
from .models              import *
from deco.utils           import token_reader

import json

class PostView(View):
    @token_reader
    def post(self, request):
        try:
            data = json.loads(request.body)
            
            Post.objects.create(
                user        = request.user,
                title       = data.get('title'),
                content     = data.get('content'),
                image_url   = data.get('image_url'),
            )
            
            return JsonResponse({"MESSAGE":"SUCCESS"}, status=201)

        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)
    
    def get(self, request):
        posts  = Post.objects.all()
        result = []
        for post in posts:
            result.append({
                'user_name'   : post.user.name,
                'content'     : post.content,
                'image_url'   : post.image_url,
                'title'       : post.title,
                'created_time': post.created_time
            }) 

        return JsonResponse({"MESSAGE": result}, status=200)


class PostDetailView(View):
    @token_reader
    def delete(self, request, post_id):
        try:
            if not Post.objects.filter(id=post_id, user_id=request.user).exists():
                return JsonResponse({"message": "NOT_EXIST_POST"}, status=400)

            Post.objects.filter(id=post_id, user_id=request.user).delete()
            return JsonResponse({"MESSAGE": "SUCCESS_DELETE"}, status=200)

        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)


    @token_reader
    def patch(self, request, post_id):
        try:
            data=json.loads(request.body)
            if not Post.objects.filter(id=post_id, user_id=request.user).exists():
                    return JsonResponse({"message": "NOT_EXIST_POST"}, status=400)
            
            post = Post.objects.get(id=post_id, user_id=request.user)
            
            post.title        = data.get('title', post.title)
            post.content      = data.get('content', post.content)
            post.image_url    = data.get('image_url', post.image_url)
            post.created_time = data.get('created_time', post.created_time)
  
            post.save()
            
            return JsonResponse({"MESSAGE": "SUCCESS_UPDATE"}, status=200)
        
        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)
    
    @token_reader
    def get(self, request):
        result=[]
        posts = Post.objects.filter(user_id=request.user)
        if not Post.objects.filter(user_id=request.user):
            return JsonResponse({"message" : "not_exits"}, status=400)
        
        for post in posts:
            result.append({
                "name"         : post.user.name,
                "title"        : post.title,
                "content"      : post.content,
                "created_tiem" : post.created_time
            })
        
        return JsonResponse({"MESSAGE": result}, status=200)
             

class CommentView(View):
    @token_reader
    def post(self, request):
        try:
            data = json.loads(request.body)
            
            if not Post.objects.filter(title=data['title']).exists():
                return JsonResponse({"message": "NOT_EXIST_POST"}, status=400)

            Comment.objects.create(
                user       = request.user,
                post       = Post.objects.get(title=data['title']),
                content    = data.get('content'),
                comment_id = data.get('comment_id')
            )
            return JsonResponse({"MESSAGE":"SUCCESS"}, status=201)
        
        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)

    def get(self, request, posting_id):
        result   = []
        
        comments =  Comment.objects.filter(comment_id=None)
        for comment in comments:
            recoments = []
            if Comment.objects.filter(comment_id = comment.id).exists():
                for recoment in Comment.objects.filter(comment_id = comment.id):
                    recoments.append({
                        "user"       : recoment.user.name,
                        "post_title" : recoment.post.title
                    })
        
            result.append({
                "comment_id" : comment.id,
                "user_name"  : comment.user.name,
                "post_title" : comment.post.title,
                "content"    : comment.content,
                "recomment"  : recoments if True else None
            })
        return JsonResponse({"MESSAGE": result}, status=200)

class CommentDetailView(View):
    @token_reader
    def delete(self, request, comment_id):
        try:
            if not Comment.objects.filter(id=comment_id, user_id=request.user).exists():
                return JsonResponse({"message": "NOT_EXIST_COMMENT"}, status=400)
            

            Comment.objects.filter(id=comment_id, user_id=request.user).delete()
            return JsonResponse({"MESSAGE": "DELETE"}, status=200)

        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)




class LikeView(View):
    @token_reader
    def post(self, request):
        try:
            data = json.loads(request.body)
            
            post_id = Post.objects.get(title=data['title']).id
            
            if not Post.objects.filter(title=data['title']).exists():
                    return JsonResponse({"message": "NOT_EXIST_POST"}, status=400)
            
            if Like.objects.filter(user=request.user, post=post_id, like='True').exists():
                Like.objects.filter(user=request.user, post=post_id, like='True').delete()
                return JsonResponse({"MESSAGE":"UNLIKE"}, status=201)

            Like.objects.create(
                user = request.user,
                post = Post.objects.get(title=data['title']),
                like = data.get('like')               
            )
            return JsonResponse({"MESSAGE":"SUCCESS"}, status=201)
        
        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)
    
    def get(self, request):
        likes = Like.objects.all()
        result=[]
        for like in likes:
            result.append({
                "user_name"  : like.user.name,
                "post_title" : like.post.title,
                "like"       : like.like
            })
        return JsonResponse({"MESSAGE": result}, status=200)

class FollowView(View):
    @token_reader
    def post(self, request):
        try:
            data      = json.loads(request.body)
            following = User.objects.get(email = data['followed_user'] ).id

            if Follow.objects.filter(user=request.user, follow_user=following).exists():
                Follow.objects.filter(user=request.user, follow_user=following).delete()
                return JsonResponse({"MESSAGE":"UN_FOLLOW"}, status=201)

            Follow.objects.create(
                user           = request.user,
                follow_user    = User.objects.get(email=data['followed_user'])
            )
            return JsonResponse({"MESSAGE":"SUCCESS"}, status=201)

        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)

    def get(self, request):
        follows = Follow.objects.all()
        result=[]
        for follow in follows:
            result.append({
                "user_name"          : follow.user.name,
                "followed_user_name" : follow.follow_user.name
            })
        return JsonResponse({"MESSAGE": result}, status=200)




