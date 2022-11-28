from rest_framework.serializers import ModelSerializer,SerializerMethodField
from .models import Post,Comment

class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class CommentSerializer(ModelSerializer):
    user_email = SerializerMethodField('get_user_email')
    post_title = SerializerMethodField('get_post_title')
    class Meta:
        model = Comment
        fields = ['post_title','user_email','comment','post','user']
    
    def get_user_email(self,obj):
        return obj.user.email
    
    def get_post_title(self,obj):
        return obj.post.title