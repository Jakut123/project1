from rest_framework import serializers

from main.models import Category, Music, Comment, Favorites, Rating


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        exclude = ['user']

    def is_liked(self, music):
        try:
            user = self.context.get('request').user
            return user.liked.filter(music=music).exists()
        except Exception:
            return False

    def in_favorites(self, music):
        try:
            user = self.context.get('request').user
            return user.favorites.filter(music=music).exists()
        except Exception:
            return False

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['is_liked'] = self.is_liked(instance)
        representation['in_favorites'] = self.in_favorites(instance)
        user = self.context.get('request').user
        if user.is_authenticated:
            representation['is_liked'] = self.is_liked(instance)
            representation['in_favorites'] = self.in_favorites(instance)
        representation['likes_count'] = instance.liked.count()
        representation['rating_count'] = instance.rating.all().count()
        rating_data = RatingSerializer(instance.rating.all(), many=True).data
        try:
            total = 0
            for ordered_dict in rating_data:
                total += ordered_dict.get('rating')
            representation['rating_average'] = total / instance.rating.all().count()
            return representation
        except ZeroDivisionError:
            return representation

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
        fields = ['id', 'music', 'text', 'created_at']

    def create(self, validated_data):
        user = self.context.get('request').user
        validated_data['user'] = user
        return super().create(validated_data)


class FavoritesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorites
        fields = ['id', 'music']

    # def validate(self, attrs):
    #     print('ffffff')
    #     if not self.context.get('request').user.IsAuthenticated:
    #         raise serializers.ValidationError('Вы не авторизованы')
    #     return attrs


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['music', 'rating', 'id']

    def validate(self, attrs):
        user = self.context.get('request').user
        music = attrs.get('music')
        try:
            rating = Rating.objects.filter(user=user)[0]
            ratings = Rating.objects.filter(music=music)
            if rating in ratings:
                raise serializers.ValidationError('Вы уже оставили отзыв')
            return attrs
        except IndexError:
            return attrs

    def create(self, validated_data):
        user = self.context.get('request').user
        validated_data['user'] = user
        return super().create(validated_data)

