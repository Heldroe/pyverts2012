from django.forms import ModelForm
from elements.models import Element

class ElementCreateForm(ModelForm):
    class Meta:
        model = Element
        fields = ('name', 'description') # should be name + location

class ElementEditForm(ModelForm):
    class Meta:
        model = Element
        fields = ('description',)