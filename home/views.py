from .serializers import (
    BlogSerializer,
    AddCommentSerializer,
    CommentSerializer,
    BlogLikeSerializer,
)
from django.db.models import Q
from rest_framework.views import APIView
from .models import Blog, Comment
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class AllBlogView(APIView):
    """
    holds two endpoints for getting all the blogs and creating a new blog.
    """

    authentication_classes = [TokenAuthentication]

    def get(self, request):
        """
        returns all the blogs from the database.
        """
        blogs = Blog.objects.all().order_by("-date_created")
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        """
        {
        "title" : str,
        "body" : str,
        "category" : str,
        "user" : int
        }
        creates a blog on the database with the associated user.
        """
        serializer = BlogSerializer(data=request.data, context={"user": request.user})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)


class PostComment(APIView):
    """
    holds one single endpoint to create a comment on a blog.

    """

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self, id):
        """
        returns the blog with the given id.
        """
        post = Blog.objects.get(id=id)
        return post

    def post(self, request, id):
        """
        adds a comment to a blog of associated id and user.
        {
        "comment" : str
        }
        """
        blog = self.get_queryset(id=id)
        serializer = AddCommentSerializer(
            data=request.data, context={"user": request.user, "blog": blog}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ShowCommentsView(APIView):
    """
    holds one endpoint that returns all the comments of an associated blog.
    """

    def get_queryset(self, id):
        """ "
        returns the blog with the given id.
        """
        blog = Blog.objects.get(id=id)

        return Comment.objects.filter(blog=blog)

    def get(self, request, id):
        """
        returns all the comments of the blog with the given id.
        """
        blog = self.get_queryset(id=id)
        serializer = CommentSerializer(blog, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class AddLikeToBlog(APIView):
    """
    holds two endpoints for getting the number of likes in a blog and adding a like to a blog.
    """

    authentication_classes = [TokenAuthentication]

    def get_queryset(self, id):
        """
        return the blog with the given id.
        """
        return Blog.objects.get(id=id)

    def get(self, request, id):
        """
        returns the number of likes for the blog with the given id.
        """
        blog = self.get_queryset(id=id)
        if request.user in blog.likes.all():
            return Response({"liked": True, "likes": len(blog.likes.all())})
        else:
            return Response({"liked": False, "likes": len(blog.likes.all())})

    def post(self, request, id):
        """
        posts a like to the blog with the given id and user.
        """
        blog = self.get_queryset(id=id)
        serializer = BlogLikeSerializer(
            data=request.data, context={"user": request.user, "blog": blog}
        )
        if serializer.is_valid():

            serializer.save()
            if request.user in blog.likes.all():
                return Response({"liked": True, "likes": len(blog.likes.all())})
            else:
                return Response({"liked": False, "likes": len(blog.likes.all())})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FilterSearch(APIView):
    """
    holds one single end point for the search of blogs.
    """

    def get_queryset(self, query):
        """
        returns all the blogs with the given category and title.
        """
        return Blog.objects.filter(
            Q(category__contains=query) | Q(title__contains=query)
        )

    def get(self, request):
        """
        returns all the blogs with the given category and title.
        """
        query = request.GET["query"]
        blogs = self.get_queryset(query=query)
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class DetailBlog(APIView):
    """
    holds one single end point for return a particular blog of given id
    """

    def get_queryset(self, id):
        """ """
        return Blog.objects.get(id=id)

    def get(self, request, id):
        blog = self.get_queryset(id=id)
        serializer = BlogSerializer(blog)
        return Response(serializer.data, status=status.HTTP_200_OK)
