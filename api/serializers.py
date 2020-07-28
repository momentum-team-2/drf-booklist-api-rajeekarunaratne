from rest_framework import serializers
from .models import Book, User, Note

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'url',
            'username',
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
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()    
    )
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