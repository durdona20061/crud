from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serialazer import *


class MoviApiView(APIView):
    def get(self, request):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(data=serializer.data)

    def post(self, request):
        serializer = MovieSerializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data)


class MovieId(APIView):

    def get(self, request, pk):

        try:
            movie = Movie.objects.get(pk=pk)
            serializer = MovieSerializer(movie)
            return Response(data=serializer.data)
        except Exception as e:
            return Response(data={'error': f'{e}'})

    def put(self, request, pk):

        try:
            movie = Movie.objects.get(pk=pk)
            serializer = MovieSerializer(movie, data=self.request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(data=self.request.data)
        except Exception as e:
            return Response(data={'error': f'{e}'})

    def patch(self, request, pk):

        try:
            movie = Movie.objects.get(pk=pk)
            serializer = MovieSerializer(movie, data=self.request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(data=self.request.data)
        except Exception as e:
            return Response(data={'error': f'{e}'})

    def delete(self, request, pk):

        try:
            movie = Movie.objects.get(pk=pk)
            movie.delete()
            return Response(data={'message': f'{pk} id delete'})
        except Exception as e:
            return Response(data={'error': f'{e}'})


class ActorAPiView(APIView):
    def get(self, request):
        actor = Actor.objects.all()
        serializer = Actorserializer(actor, many=True)
        return Response(data=serializer.data)

    def post(self, request):
        serializer = Actorserializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data)


class ActorApiId(APIView):

    def get(self, request, pk):
        try:
            actor = Actor.objects.get(pk=pk)
            serializer = Actorserializer(actor)
            return Response(data=serializer.data)
        except Exception as e:
            return Response(data={'error': f'{e}'})

    def put(self, request, pk):
        try:
            actor = Actor.objects.get(pk=pk)
            serializer = Actorserializer(actor, data=self.request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(data=self.request.data)
        except Exception as e:
            return Response(data={'error': f'{e}'})

    def patch(self, request, pk):
        try:
            actor = Actor.objects.get(pk=pk)
            serializer = Actorserializer(actor, data=self.request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(data=self.request.data)
        except Exception as e:
            return Response(data={'error': f'{e}'})

    def delete(self, request, pk):
        try:
            actor = Actor.objects.get(pk=pk)
            actor.delete()
            return Response(data={'message': f'{pk} id delete'})
        except Exception as e:
            return Response(data={'error': f'{e}'})
