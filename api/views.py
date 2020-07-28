from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend, OrderingFilter
from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from .models import User, Note, Book
from .serializers import UserSerializer, NoteSerializer, BookSerializer
from .permissions import IsOwner



# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_class = [permissions.IsAuthenticated]

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_class = [permissions.IsAuthenticated, IsOwner]
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ['status']


    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_class = [permissions.IsAuthenticated]

