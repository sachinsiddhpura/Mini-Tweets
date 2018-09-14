from django.contrib import admin

# Register your models here.
from .models import Tweet
from .forms import TweetForm

#admin.site.register(Tweet)

class TweetFormAdmin(admin.ModelAdmin):
	form=TweetForm
	#class Meta:
	#	model = Tweet

admin.site.register(Tweet,TweetFormAdmin)

