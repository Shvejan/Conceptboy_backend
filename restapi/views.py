from django.contrib.auth.models import User, Group
from rest_framework import viewsets,permissions
from .models import Snippet,Video,Subject,Category,Subcategory
from .serializers import UserSerializer, GroupSerializer,SnippetSerialiser,SubjectSerialiser,CategorySerialiser,SubcategorySerialiser,VideoSerialiser


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class SnippetViewset(viewsets.ModelViewSet):
    queryset = Snippet.objects.all()
    serializer_class=SnippetSerialiser



class SubjectViewset(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class=SubjectSerialiser

class CategoryViewset(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class=CategorySerialiser

class SubcategoryViewset(viewsets.ModelViewSet):
    queryset = Subcategory.objects.all()
    serializer_class=SubcategorySerialiser

class VideoViewset(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    # permission_classes=[
    # permissions.AllowAny
    # ]
    serializer_class=VideoSerialiser
