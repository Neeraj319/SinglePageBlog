from django.urls import path, include
from .views import *
urlpatterns = [
    # path('' , include(router.urls)),
    path('login', LoginView.as_view()),
    path('signup', SignUp.as_view()),
    path("user/<str:username>", UserProfile.as_view()),
    path("username", GetUsername.as_view()),
    path('userblogs', GetUserBlogs.as_view())
]
