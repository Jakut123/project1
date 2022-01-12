from rest_framework import serializers

from main.models import Category, Music, Comment, Favorites


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = ['title', 'author', 'image', 'music', 'description', 'created_at', 'category']

    def create(self, validated_data):
        validated_data['user'] = self.context.get('request').user
        return super().create(validated_data)


class MusicListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = ['title', 'author', 'image', 'created_at']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class FavoritesSerializer(serializers.Serializer):
    class Meta:
        model = Favorites
        fields = '__all__'

