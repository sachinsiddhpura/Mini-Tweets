from rest_framework import serializers
from tweets.models import Tweet 
from accounts.api.serializers import UserDisplaySeri
from django.utils.timesince import timesince

class TweetSerializer(serializers.ModelSerializer):
	user=UserDisplaySeri(read_only=True)
	date_display=serializers.SerializerMethodField()
	timesince=serializers.SerializerMethodField()
	class Meta:
		model 	=Tweet
		fields	=('user','content','date_display','timestamp','timesince',)

	def get_date_display(self,obj):
		return obj.timestamp.strftime("%b %d, %Y at %I:%M %p")

	def get_timesince(self,obj):
		return timesince(obj.timestamp) + "ago"