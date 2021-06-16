from django.urls import path, include
from django.utils.translation import deactivate
from rest_framework import routers
from rest_framework.routers import DefaultRouter
from .views import *
from graphene_django.views import GraphQLView
from .schema import schema

# router = DefaultRouter()
# router.register('' , BlogsView)
urlpatterns = [
    # path('' , include(router.urls)),
    path("", AllBlogView.as_view()),
    path("add_comment/<int:id>", PostComment.as_view()),
    path("comments/<int:id>", ShowCommentsView.as_view()),
    path("like_blog/<int:id>", AddLikeToBlog.as_view()),
    path("search", FilterSearch.as_view()),
    path("blog/<int:id>", DetailBlog.as_view()),
    path("graphql", GraphQLView.as_view(graphiql=True, schema=schema)),
]
