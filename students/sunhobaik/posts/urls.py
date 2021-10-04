from django.urls import path, include
from .views import *
urlpatterns = [
    path('/post', PostView.as_view()),
    path('/post/detail', PostDetailView.as_view()),
    path('/post/detail/<int:post_id>', PostDetailView.as_view()),
    path('/comment', CommentView.as_view()),
    path('/comment/<int:posting_id>', CommentView.as_view()),
    path('/comment/delete/<int:comment_id>', CommentDetailView.as_view()),
    path('/like', LikeView.as_view()),
    path('/follow', FollowView.as_view()),
]