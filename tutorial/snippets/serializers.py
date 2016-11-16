from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User


# first part defines fields to be serialized/deserialized
# create/update methods define how instances are affected by serializer.save()
class SnippetSerializer(serializers.ModelSerializer):
   class Meta:
        model = Snippet
        fields = ('id', 'title', 'code', 'lineos', 'language', 'style')
        owner = serializers.ReadOnlyField(source='owner.username')


# serializer to interact with Users
class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True,
            queryset=Snippet.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'snippets')
