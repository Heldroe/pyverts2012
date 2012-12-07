from django.forms import ModelForm
from django import forms
from team360.models import Rating

class RateUserForm(ModelForm):
	value = forms.ChoiceField(widget=forms.RadioSelect(), choices=Rating.BAR_CHOICES)
	class Meta:
		model = Rating
		fields = ('value',)


