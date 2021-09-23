from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User


class SnippetSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlighted = serializers.HyperlinkedIdentityField(view_name='snippet-highlighted',format='html')
    class Meta:
        model=Snippet
        fields=('url','id','highlighted','owner','title','code','lineos','language','styles')
        
class UserSerializer(serializers.ModelSerializer):
    snippets=serializers.HyperlinkedRelatedField(many=True,view_name='snippet-detail',read_only=True)
    
    class Meta:
        model=User
        fields=('url','id','username','snippets')