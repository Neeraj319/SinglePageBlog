from django.urls import path
from . import views

urlpatterns = [
    path("", views.AllBlogView.as_view()),
    path("add_comment/<int:id>", views.PostComment.as_view()),
    path("comments/<int:id>", views.ShowCommentsView.as_view()),
    path("like_blog/<int:id>", views.AddLikeToBlog.as_view()),
    path("search", views.FilterSearch.as_view()),
    path("blog/<int:id>", views.DetailBlog.as_view()),
]
