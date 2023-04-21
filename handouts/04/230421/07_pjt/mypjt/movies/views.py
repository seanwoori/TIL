from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_list_or_404, get_object_or_404
from .models import Actor, Movie, Review
from .serializers import ActorSerializer, ReviewDetailSerializer, MovieDetailSerializers, MovieSerializer, ReviewSerializer, ActorDetailSerializer

# Create your views here.
@api_view(['GET'])
def actor_list(request):
    if request.method == "GET":
        actors = get_list_or_404(Actor)
        serializer = ActorSerializer(actors, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def actor_detail(request, actor_pk):
    actor = get_object_or_404(Actor, pk=actor_pk)
    if request.method == "GET":
        serializer = ActorDetailSerializer(actor)
        return Response(serializer.data)


@api_view(['GET'])
def movie_list(request):
    if request.method == "GET":
        movies = get_list_or_404(Movie)
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.method == "GET":
        serializer = MovieDetailSerializers(movie)
        return Response(serializer.data)
    

@api_view(['GET'])
def review_list(request):
    if request.method == "GET":
        reviews = get_list_or_404(Review)
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)
    
     
@api_view(['GET', 'PUT', 'DELETE'])
def review_detail(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if request.method == "GET":
        serializer = ReviewDetailSerializer(review)
        return Response(serializer.data)
    elif request.method == "DELETE":
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == "PUT":
        serializer = ReviewDetailSerializer(review, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


@api_view(['POST'])
def create_review(request):
    if request.method == "POST":
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)