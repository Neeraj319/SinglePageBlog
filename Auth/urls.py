from django.urls import path , include
from .views import *
urlpatterns = [
    # path('' , include(router.urls)),
    path('login' , LoginView.as_view()),
]