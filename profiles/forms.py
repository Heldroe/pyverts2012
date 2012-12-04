from django.forms import ModelForm
from profiles.models import UserProfile

class ProfileEditForm(ModelForm):
	class Meta:
		model = UserProfile
		fields = ('test',)

class ProfileAvatarForm(ModelForm):
	class Meta:
		model = UserProfile
		fields = ('avatar',)