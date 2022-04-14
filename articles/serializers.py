from rest_framework.serializers import Serializer, ModelSerializer, CharField
from articles.models import *
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.settings import api_settings
from django.contrib.auth.models import update_last_login
from django.core.exceptions import ObjectDoesNotExist


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


# class CommentSerializer(ModelSerializer):
#     class Meta:
#         model = Comment
#         fields = '__all__'

class SubSubCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        
class SubCommentSerializer(serializers.ModelSerializer):
    comment = SubSubCommentSerializer()
    class Meta:
        model = Comment
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    parent_comment = serializers.PrimaryKeyRelatedField(read_only=True)
    comment = SubCommentSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'
        # extra_kwargs = {
        #     'comment_id': {'source': 'comment', 'write_only': True},
        # }


class ArticleSerializer(ModelSerializer):
    comment = CommentSerializer(read_only=True, many=True)
    class Meta:
        model = Article
        fields = '__all__'
