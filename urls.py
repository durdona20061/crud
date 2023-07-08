from django.urls import path
from .views import *

urlpatterns = [
    path('movieId/<int:pk>', MovieId.as_view()),
    path('movie/', MoviApiView.as_view()),
    path('actor/', ActorAPiView.as_view()),
    path('actorId/<int:pk>', ActorApiId.as_view())
]
