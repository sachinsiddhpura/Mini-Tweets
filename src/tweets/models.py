from django.db import models

# Create your models here.
from django.conf import settings
from django.urls import reverse

class Tweet(models.Model):
	user	=models.ForeignKey(settings.AUTH_USER_MODEL)
	content	=models.CharField(max_length=120)
	updated	=models.DateTimeField(auto_now=True)
	timestamp	=models.DateTimeField(auto_now_add=True)
	post	=models.FileField(blank=True,null=True)

	def __str__(self):
		return str(self.content)

	def get_absolute_url(self):
		return reverse("tweet:detail",kwargs={"pk":self.pk})