from rest_framework import serializers
from projects.models import Project, Tag
from users.models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    """
    serialize users model data
    """
    class Meta:
        model = Profile
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    """
    serialize tag model data
    """
    class Meta:
        model = Tag
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    """
    serialize Project model data and set some model fields to another serialized objects to gain
    access to dynamic data thru project serializer itself
    """
    owner = ProfileSerializer(many=False)
    tags = TagSerializer(many=True)

    class Meta:
        model = Project
        fields = '__all__'