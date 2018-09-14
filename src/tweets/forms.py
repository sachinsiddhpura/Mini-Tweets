from django import forms
from .models import Tweet

class TweetForm(forms.ModelForm):
	content=forms.CharField(label='',
		widget=forms.Textarea(attrs={"placeholder":"Your Message","class":"form-control"}))
	class Meta:
		model =Tweet
		fields=('content','post',)

	def clean_content(self,*args,**kwargs):
		content=self.cleaned_data.get("content")
		if content =="abc":
			raise forms.ValidationError("cannot content abc")
		return content