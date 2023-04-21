from rest_framework import serializers
from .models import Actor, Movie, Review

class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'
    

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'   


class MovieDetailSerializers(serializers.ModelSerializer):
    class ActorSerializer(serializers.ModelSerializer):
        class Meta:
            model = Actor
            fields = ('name',)

    class ReviewSerializer(serializers.ModelSerializer):
        class Meta:
            model = Review
            fields = ("title",)   

    class Meta:
        model = Movie
        fields = ('title','overview','release_date', 'poster_path', 'actors', 'review' )

    actors = ActorSerializer(many=True)
    review = ReviewSerializer(many=True)


class ActorDetailSerializer(serializers.ModelSerializer):
    class MovieSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ('title',)

    class Meta:
        model = Actor
        fields = ('id', 'movie', 'name',)
    
    movie = MovieSerializer(many=True)


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"


class ReviewDetailSerializer(serializers.ModelSerializer):
    class MovieSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ('title',)

    class Meta:
        model = Review
        fields = ('id', 'title', 'content', 'movie',) 

    movie = MovieSerializer()