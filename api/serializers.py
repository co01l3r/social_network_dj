from rest_framework import serializers
from projects.models import Project, Tag, Review
from users.models import Profile


class ReviewSerializer(serializers.ModelSerializer):
    """
    serialize users model data
    """
    class Meta:
        model = Review
        fields = '__all__'


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
    reviews = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = '__all__'

    def get_reviews(self, object):
        """
        add reviews as object to fields to gain access
        """
        reviews = object.review_set.all()
        serializer = ReviewSerializer(reviews, many=True)
        return serializer.data
