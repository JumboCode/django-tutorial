from rest_framework import routers
from django.urls import path

from .models import *
from .views import *

urlpatterns = [
    path("sleds/", ListSledsRaw.as_view(), name="sled-list"),
    path("members/", MembersList.as_view(), name="members-list")

]

