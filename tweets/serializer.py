from rest_framework import serializers
from twitter.settings import MAX_TWEET_LENGTH
from .models import Tweet


class TweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = ['content','likes']

    def validate_content(self, value):
        if len(value) > MAX_TWEET_LENGTH:
            raise serializers.ValidationError('Tweet too long, the app is just a mockup')
        return value