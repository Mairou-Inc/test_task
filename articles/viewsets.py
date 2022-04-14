from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from rest_framework.authentication import TokenAuthentication, BasicAuthentication, SessionAuthentication
from rest_framework import viewsets, permissions
from rest_framework import status
from rest_framework import generics
from articles.models import *

from rest_framework.decorators import api_view

from rest_framework.authtoken.models import Token


class UserDetailView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = (TokenAuthentication, BasicAuthentication, SessionAuthentication)

    def get(self, request):
        serializer = UserSerializer(User.objects.get(id=request.user.id))
        return Response(serializer.data)



class ArticleView(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    # permission_classes = [permissions.IsAuthenticated]
    # authentication_classes = (TokenAuthentication, BasicAuthentication)

    def list(self, request, pk=None):
        queryset = Article.objects.all()
        serializer = ArticleSerializer(queryset, context={'request': request}, many = True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        return super().retrieve(request)

class CommentView(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    # permission_classes = [permissions.IsAuthenticated]
    # authentication_classes = (TokenAuthentication, BasicAuthentication)

    def list(self, request, pk=None):
        if pk:
            queryset = Comment.objects.filter(article_id=pk)
        else:   
            queryset = Comment.objects.all()
        serializer = CommentSerializer(queryset, context={'request': request}, many = True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        return super().retrieve(request)

