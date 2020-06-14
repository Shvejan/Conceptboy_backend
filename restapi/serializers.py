from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Video,Category,Subcategory,Subject
from .models import Snippet


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id','url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class SnippetSerialiser(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Snippet
        fields = ['id','created', 'url','title', 'code']

class VideoSerialiser(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Video
        fields = ['id','name', 'url','video_url', 'category','subcategory']


class SubjectSerialiser(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Subject
        fields = ["id",'url','name']

class CategorySerialiser(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ["id",'url','name']

class SubcategorySerialiser(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Subcategory
        fields = ["id",'url','name']
