from tweets.models import Tweet
from tweets.serializer import TweetSerializer
from rest_framework import viewsets


# Create your views here.

class TweetView(viewsets.ModelViewSet):
    serializer_class = TweetSerializer
    queryset = Tweet.objects.all()


