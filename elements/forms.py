from django.forms import ModelForm
from elements.models import Element, Photo

class ElementCreateForm(ModelForm):
    class Meta:
        model = Element
        fields = ('name', 'description') # should be name + location

class ElementEditForm(ModelForm):
    class Meta:
        model = Element
        fields = ('description',)

class PhotoAddForm(ModelForm):
	class Meta:
		model = Photo
		fields = ('picture', 'title', 'description')