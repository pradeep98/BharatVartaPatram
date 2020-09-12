from rest_framework import serializers
from patram.models import Post

class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'description','content']