from rest_framework import serializers

from .models import Link, Collection


class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = '__all__'
        read_only_fields = ['user', 'title', 'description', 'image', 'link_type', 'created_at', 'updated_at']


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = '__all__'
        read_only_fields = ['user', 'created_at', 'updated_at']
