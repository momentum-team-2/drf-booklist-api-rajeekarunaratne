from rest_framework import serializers
from .models import Book, User, Note

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'url',
            'username',
            'is_staff',
        ]

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = [
            'book',
            'time_stamp',
            'note',
            'page_number',
        ]

class BookSerializer(serializers.HyperlinkedModelSerializer):
    notes = NoteSerializer(many=True, read_only=True)

    class Meta:
        model = Book
        fields = [
            'url',
            'user',
            'title',
            'author',
            'status',
            'notes',
        ]