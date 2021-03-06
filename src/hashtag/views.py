from django.shortcuts import render

# Create your views here.
from django.views import View
from .models import HashTag

class HashView(View):
	def get(self,request,hashtag,*args,**kwargs):
		obj, created=HashTag.objects.get_or_create(tag=hashtag)
		return render(request,"tag_view.html",{"obj",obj})