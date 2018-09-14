from rest_framework import generics
from tweets.models import Tweet
from .serializers import TweetSerializer
from django.db.models import Q
from rest_framework import permissions
from .pagination import StandardPagination

class TweetCreateAPI(generics.CreateAPIView):
	serializer_class	=TweetSerializer
	permission_classes	=[permissions.IsAuthenticated]

	def perform_create(self,serializer):
		serializer.save(user=self.request.user)


class TweetListAPI(generics.ListAPIView):
	serializer_class	=TweetSerializer
	pagination_class	=StandardPagination

	def get_queryset(self,*args,**kwargs):
		queryset=Tweet.objects.all().order_by("-timestamp")
		query=self.request.GET.get("q",None)
		if query is not None:
			queryset=queryset.filter(
					Q(content__icontains=query)
				)
		return queryset