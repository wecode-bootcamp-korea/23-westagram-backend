from django.db import models


class Post(models.Model):
    user         = models.ForeignKey('users.User', on_delete=models.CASCADE)
    title        = models.CharField(max_length=200)
    content      = models.TextField(max_length=2000, null=True)
    image_url    = models.CharField(max_length=1000, null=True)
    created_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "posts"

class Comment(models.Model):
    user       = models.ForeignKey("users.User", on_delete=models.CASCADE)
    post       = models.ForeignKey("Post", on_delete=models.CASCADE) 
    content    = models.CharField(max_length=500, null=True)
    comment    = models.ForeignKey("self", on_delete=models.SET_NULL, null=True, related_name='recomment')
 
    
    class Meta:
        db_table = "comments"

class Like(models.Model):
    user  = models.ForeignKey("users.User", on_delete=models.CASCADE)
    post  = models.ForeignKey("Post", on_delete=models.CASCADE)
    like  = models.BooleanField(null=True)

    class Meta:
        db_table = "likes"

class Follow(models.Model):
    user        = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="follower")
    follow_user = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="followed_user")

    class Meta:
        db_table = "follows" 