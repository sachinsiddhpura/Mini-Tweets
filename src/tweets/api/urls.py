from django.conf.urls import url, include
from django.contrib import admin

from django.conf import settings
#from django.conf.urls.static import static
from .views import TweetListAPI, TweetCreateAPI
#from tweets.views import Tweetlist


urlpatterns = [
	url(r'^$', TweetListAPI.as_view(),name="listapi"),
	url(r'^create/$', TweetCreateAPI.as_view(),name="createapi"),
    #url(r'^admin/', admin.site.urls),
    #url(r'^$', Tweetlist.as_view(),name="home"),
    #url(r'^tweetme/', include('tweets.urls', namespace='tweet')),
    #url(r'^api/tweetme/', include('tweets.urls', namespace='tweetapi')),
]
