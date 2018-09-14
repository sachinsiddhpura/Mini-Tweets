from django.conf.urls import url, include
from .views import (
	tcreate,
	tdetail,
	Tweetlist,
	TweetCreate,
	TweetUpdate,
	TweetDelete,
	TweetDetail,
	)
from django.views.generic.base import RedirectView

urlpatterns = [
	#url(r'^gmail/$',gmail, name='e'),
	url(r'^$',RedirectView.as_view(url='/')),
	url(r'^create/$',TweetCreate.as_view(), name='create'),
	url(r'^search/$',Tweetlist.as_view(), name='list'),
	#url(r'^(?P<id>\d+)/$',tdetail, name='detail'),
	url(r'^(?P<pk>\d+)/$',TweetDetail.as_view(), name='detail'),
	url(r'^(?P<pk>\d+)/update/$',TweetUpdate.as_view(), name='update'),
	url(r'^(?P<pk>\d+)/delete/$',TweetDelete.as_view(), name='delete'),
	#url(r'^create/$',tcreate, name='create'),
    #url(r'^admin/', admin.site.urls),
    #url(r'^$', home),
    #url(r'^tweetme/', include('tweets.urls')),
]