from django.shortcuts import render, get_object_or_404,HttpResponseRedirect,HttpResponse

# Create your views here.
from .models import Tweet
from django.db.models import Q
from django.views.generic import DetailView,ListView, CreateView, UpdateView, DeleteView
from .forms import TweetForm
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import FormUserNeededMixin
from django.urls import reverse_lazy
from django.conf import settings
from django.core.mail import send_mail, BadHeaderError


class TweetDelete(LoginRequiredMixin, DeleteView):
	model = Tweet
	template_name='tweets/delete_view.html'
	success_url=reverse_lazy("tweet:list")

class TweetUpdate(UpdateView):
	queryset=Tweet.objects.all()
	form_class=TweetForm
	template_name='tweets/update_view.html'
	success_url='/tweetme/'

class TweetCreate(LoginRequiredMixin, FormUserNeededMixin, CreateView):
	form_class=TweetForm
	template_name='tweets/create_view.html'
	success_url='/hello/'
	login_url='/admin/'


class TweetDetail(DetailView):
	queryset=Tweet.objects.all()


def tcreate(request):
	form=TweetForm(request.POST or None)
	if form.is_valid():
		obj=form.save(commit=False)
		obj.save()
		return HttpResponseRedirect("/tweetme/{num}".format(num=obj.id))
	context={
		"form":form
	}
	template='form.html'
	return render(request,template,context)


class Tweetlist(ListView):

	def get_queryset(self,*args,**kwargs):
		queryset=Tweet.objects.all()
		query=self.request.GET.get("q",None)
		if query is not None:
			queryset=queryset.filter(
					Q(content__icontains=query)
				)
		return queryset

	def get_context_data(self,*args,**kwargs):
		context=super(Tweetlist,self).get_context_data(*args,**kwargs)
		context['form']=TweetForm()
		context['create_url']=reverse_lazy("tweet:create")
		return context


def tdetail(request,id=None):
	qs=get_object_or_404(Tweet,id=id)
	context={
		"qs":qs
	}
	template="detail.html"
	return render(request,template,context)
'''
def tlist(request):
	query=request.GET.get('q',None)
	qs1=Tweet.objects.all()
	if query is not None:
		qs1=qs1.filter(
			Q(content__icontains=query)
			)
	context={
		"qs1":qs1
	}
	template="list.html"
	return render(request,template,context)'''