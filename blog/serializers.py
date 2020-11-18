from rest_framework import serializers
from .models import Blog

class BlogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Blog
        fields = ('id', 'title', 'headline', 'body', 'created_at', 'heading_img_link', 'sub_img_link_1', 'sub_img_link_2', 'sub_img_link_3', 'sub_img_link_4', 'sub_img_link_5')