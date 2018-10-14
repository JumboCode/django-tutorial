from django.shortcuts import render
from django.shortcuts import get_object_or_404


# Create your views here.

from .models import *
from .serializers import *

from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import generics

#
# There are many ways to write a view!
# Django gives alot of flexibility and abstraction
# depending how special your needs are. For simple things,
# django already has abstractions that do heavy lifting.



# If your view subclasses APIView, then the request is simply
# dispatched to a function handler named by the http method.
#
# This is great if you want raw access and control over routes.


class ListSledsRaw(APIView):

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        queryset = Sled.objects.all()
        serializer = SledSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        """
        How might a post request work?
        """
        pass


# If your view subclasses a Generic, then the request is
# dispatched to a django-generated handler. Whichever generic class
# you use determines

# This is great if you want api routes for listing items, retreiving single items,
# creating items, etc. Basically generics extend off api view and generate the get a
# and post route handlers underneath the scene.

# https://www.django-rest-framework.org/api-guide/generic-views/#retrieveapiview

# The generic you choose to subclass from determines the routes that are generated
# underneath the scenes. For instance generics.ListCreateApiView generates
# a get route for the model specified and post route that will create
# a new instance of the model with form data from the request.

# There are other generics that work over individual items, and will generate
# routes for deleting or updating a prexisting item in the database.

# This means that the ListCreate view is the same functionality as the raw APIView class above.
# Say you want to overide the generated post route tho? You can still write a custom post method
# just as before and still have the list functionality generated for you.

# Don't beleive it's the same? Trying changing the /sleds url - view mapping in urls.py and see what happens?
# Does the post route work now?

class SledList(generics.ListCreateAPIView):
     queryset = Sled.objects.all()
     serializer_class = SledSerializer

class MembersList(generics.ListCreateAPIView):
     queryset = TeamMember.objects.all()
     serializer_class = TeamMemberSerializer
#
# If your view subclasses a viewset, it's basically just a bunch of generics on
# steroids. You can also use ModelViewSets to give you viewsets based on models.
#
# Viewsets combined with routers are great ways to get maxmimum basic CRUD functionality '
# with writing as little code as possible.
#

class ShledViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = Sled.objects.all()
        serializer = SledSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Sled.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = SledSerializer(user)
        return Response(serializer.data)

    def create(self, request):
        pass

    def retrieve(self, request, pk=None):
        pass

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass