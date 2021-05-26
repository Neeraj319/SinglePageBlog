from django.urls import path , include
from django.utils.translation import deactivate
from rest_framework import routers
from rest_framework.routers import DefaultRouter
from .views import *
# router = DefaultRouter()
# router.register('' , BlogsView)
urlpatterns = [
    # path('' , include(router.urls)),
    path('' , AllBolgView.as_view()),
]