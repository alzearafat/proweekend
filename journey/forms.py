from django import forms 
from journey.models import Post
from crispy_forms.helper import FormHelper

class JourneyForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ['title', 'featured_image', 'location', 'content', 'gallery_image_1', 'gallery_image_2', 'gallery_image_3', 'gallery_image_4', 'tanggal_publish']
		exclude = ['author']
		widgets = {'author': forms.HiddenInput()}