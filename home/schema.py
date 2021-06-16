import graphene
from graphene_django import DjangoObjectType
from .models import Blog, Comment


class BlogType(DjangoObjectType):
    class Meta:
        model = Blog
        fields = ("id", "title", "body", "likes", "user", "category")


class CommentType(DjangoObjectType):
    class Meta:
        model = Comment
        fields = ("id", "text", "user", "like")


class Query(graphene.ObjectType):

    all_blogs = graphene.List(BlogType)
    get_blog = graphene.Field(BlogType, id=graphene.Int())
    all_comments = graphene.List(CommentType)
    filter_blogs = graphene.List(BlogType, category=graphene.String())

    def resolve_filter_blogs(root, info, category):
        return Blog.objects.filter(category=category)

    def resolve_all_blogs(root, info):
        return Blog.objects.all()

    def resolve_all_comments(root, info):
        return Comment.objects.all()

    def resolve_get_blog(root, info, id):
        return Blog.objects.get(id=id)


schema = graphene.Schema(query=Query)
