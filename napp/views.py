from napp.serializer import AuthorSerializer,BookSerializer
from .models import Books,Author
from rest_framework import generics
"""
this only for one class or perticulr authentication
from rest_framework.authentication import BasicAuthentication # for autentiction
from rest_framework.permissions import IsAuthenticated ,DjangoModelPermissions # for permission/Djangopermission is used for groping the perimission like user

"""

# Create your views here.
class AuthorListView(generics.ListCreateAPIView): #  for get and post
    queryset=Author.objects.all()
    serializer_class=AuthorSerializer
    """
    is for only one class authentication
    authentication_classes=[BasicAuthentication]
    permission_classes=[IsAuthenticated,DjangoModelPermissions] # this Django modelpermissiom will grope permision

    """

class AuthorDetailView(generics.RetrieveUpdateDestroyAPIView):
     queryset=Author.objects.all()
     serializer_class=AuthorSerializer


class BooksListView(generics.ListCreateAPIView):
    queryset=Books.objects.all()
    serializer_class=BookSerializer


class BooksDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Books.objects.all()
    serializer_class=BookSerializer